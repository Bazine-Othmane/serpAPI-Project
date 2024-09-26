from langchain_community.utilities.serpapi import SerpAPIWrapper
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
import os
from dotenv import load_dotenv


# Set your SerpAPI key as an environment variable
#os.environ["SERPAPI_API_KEY"] = "SERPAPI_API_KEY"
#os.environ["OPENAI_API_KEY"] = "OPENAI_API_KEY"

# Initialize the SerpAPIWrapper
serpapi = SerpAPIWrapper()

# Define your query
query = "give me information about algeria"

# Perform the search
results = serpapi.run(query)

# Process and print the results

print(results)




