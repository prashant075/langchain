from dotenv import load_dotenv


load_dotenv()

from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from langchain_ollama import ChatOllama
from tavily import TavilyClient

tavily_client = TavilyClient()

@tool
def search(query: str) -> str:
    """

    Tool that searches over internet
    Args:
        query: The query to search for
    Returns:
        The search results
    """
    print(f"Searching for {query}")
    return tavily_client.search(query=query)


llm =  ChatOllama(model="deepseek-r1:1.5b")
tools = [search]
agent = create_agent(llm, tools=tools)

def main():
    print("Starting the agent...")
    response = agent.invoke({"messages": [HumanMessage(content="search for 3 job postings for an ai engineer using langchain in the bay area on linkedin and list their details")]})
    print(response)

if __name__ == "__main__":
    main()