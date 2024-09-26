from langchain_community.utilities.serpapi import SerpAPIWrapper
from langchain_community.utilities.serpapi import SerpAPIWrapper
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
import os
from dotenv import load_dotenv


# Set your SerpAPI key as an environment variable
#os.environ["SERPAPI_API_KEY"] = "SERPAPI_API_KEY"
#os.environ["OPENAI_API_KEY"] = "OPENAI_API_KEY"

# Initialize the SerpAPIWrapper

serpapiQuery = "give me information about algeria"
# Initialize the SerpAPIWrapper
serpapi = SerpAPIWrapper()

# Define your query

# Perform the search
results = serpapi.run(serpapiQuery)

# Initialize the OpenAI language model
llm = ChatOpenAI()

# Create a prompt template
prompt_template = PromptTemplate(
    input_variables=["query", "results"],
    template=(
        "You are an AI assistant. Based on the following search results, answer the query: {query}\n\n"
        "Search Results:\n{results}\n\n"
        "Answer:"
    )
)
query="what is the capital of algeria ?"
# Format the prompt with the search results
prompt = prompt_template.format(query=query, results=results)

# Get the response from OpenAI
response = llm.invoke(prompt)
print(response)
# Print the response



