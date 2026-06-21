from dotenv import load_dotenv
from typing import List
from pydantic import BaseModel, Field


load_dotenv()

from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from langchain_ollama import ChatOllama
from langchain_tavily import TavilySearch

class  Source(BaseModel):
    """Schema for a source used by the agent"""

    url:str = Field(description="The URL of the source")

class AgentResponse(BaseModel):
   """Schema for agent response with answer and sources"""

   answer:str = Field(description="The agent's answer to the query")
   sources: List[Source] = Field(default_factory=list, description="List of sources used to generate the answer")

llm =  ChatOllama(model="deepseek-r1:1.5b")
tools = [TavilySearch()]
agent = create_agent(llm, tools=tools, response_format=AgentResponse)

def main():
    print("Starting the agent...")
    response = agent.invoke({"messages": [HumanMessage(content="search for 3 job postings for an ai engineer using langchain in the bay area on linkedin and list their details")]})
    print(response)

if __name__ == "__main__":
    main()