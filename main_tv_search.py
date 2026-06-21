from dotenv import load_dotenv


load_dotenv()

from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from langchain_ollama import ChatOllama
from langchain_tavily import TavilySearch


llm =  ChatOllama(model="deepseek-r1:1.5b")
tools = [TavilySearch()]
agent = create_agent(llm, tools=tools)

def main():
    print("Starting the agent...")
    response = agent.invoke({"messages": [HumanMessage(content="search for 3 job postings for an ai engineer using langchain in the bay area on linkedin and list their details")]})
    print(response)

if __name__ == "__main__":
    main()