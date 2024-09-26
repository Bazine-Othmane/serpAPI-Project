from serpapi import search
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain.agents import  create_tool_calling_agent,Tool
from langchain.agents.agent import AgentExecutor
import os
from langchain_community.utilities.serpapi import SerpAPIWrapper
from langchain_core.prompts import ChatPromptTemplate,MessagesPlaceholder
from langchain_core.prompts.chat import SystemMessage,HumanMessage

# SerpAPI search parameters
params = {
    "q": "give me an informations about algeria",
    "location": "Ouargla, Ouargla, Algeria",
    "hl": "en",
    "gl": "us",
    "google_domain": "google.com",
    "api_key": "SERPAPI_API_KEY"
}
os.environ["SERPAPI_API_KEY"] = "SERPAPI_API_KEY"
os.environ["OPENAI_API_KEY"] = "OPENAI_API_KEY"

# Perform the search
search = search(params).as_dict()

serpapi_wrapper = SerpAPIWrapper(params=params)

# Define the SerpAPI tool
serpapi_tool = Tool(
    name="SerpAPI",
    func=serpapi_wrapper.run,
    description="A tool to fetch search results from SerpAPI"
)


chat_prompt_template = ChatPromptTemplate.from_messages([
    SystemMessage(content="You are an agent that provides detailed answers based on following web links \n\n{search_results},Based on the your search results, Answer the question based on the above context:\n\n{query}."),
    HumanMessage(content="Based on the your search results, Answer the question based on the above context"),
    MessagesPlaceholder(variable_name="agent_scratchpad")
])


# Initialize the OpenAI model
llm = ChatOpenAI(model="gpt-3.5-turbo")

# Create the agent
agent = create_tool_calling_agent(
    llm=llm,
    tools=[serpapi_tool],
    prompt=chat_prompt_template
)

# Create the agent executor
agent_executor = AgentExecutor(agent=agent,tools=[serpapi_tool])




# Use the agent to get a response
response = agent_executor.invoke({"search_results": search, "query": 'what is the capital of algeria ?'})


print(response)






















