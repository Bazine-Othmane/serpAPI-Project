from re import VERBOSE
from langchain import hub
from langchain_openai import ChatOpenAI
from langchain.agents import create_tool_calling_agent,Tool
from langchain_community.utilities.serpapi import SerpAPIWrapper
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.tools import DuckDuckGoSearchRun
from langchain.agents import AgentExecutor
from dotenv import load_dotenv
import os
from langchain_core.prompts import ChatPromptTemplate,MessagesPlaceholder
from langchain_core.prompts.chat import SystemMessage,HumanMessage


load_dotenv()
os.environ["SERPAPI_API_KEY"] = ""
os.environ["GOOGLE_API_KEY"] = ""
query='What is the capital of algiria?'

params = {
    "q": query,
    "location": "Ouargla, Ouargla, Algeria",
    "hl": "en",
    "gl": "us",
    "google_domain": "google.com",
    "api_key": ""
}

# Configure SerpAPI with your API key

#prompt = hub.pull("hwchase17/openai-functions-agent")

custom_prompt = ChatPromptTemplate(messages=[
    SystemMessage(content="You are a helpful assistant that provides concise and accurate information using serpAPI to search on Google."),
    HumanMessage(content="Based on the your search results,i want to answer this question : What is the capital of algiria?"),
    MessagesPlaceholder(variable_name="agent_scratchpad")]
)




search_tool  = SerpAPIWrapper(params=params)
print(search_tool.run(query=query))
serpapi_tool = Tool(name="SerpAPI", func=search_tool.run,description="A tool to fetch search results from SerpAPI")


llm = ChatGoogleGenerativeAI(model="gemini-1.5-pro",temperature=0.2)

agent = create_tool_calling_agent(llm, [serpapi_tool], custom_prompt)

agent_executor = AgentExecutor(agent=agent, tools=[serpapi_tool])
response = agent_executor.invoke({"question": query,})
print(response)
