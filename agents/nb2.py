from typing import TypedDict, Annotated, operator
from langchain_core.messages import AnyMessage
from langgraph.graph import StateGraph, END
from langchain_core.language_models.chat_models import BaseChatModel
from langchain_core.tools import tool
from langchain_ollama import ChatOllama

def multiply(a, b):
    return a * b


llm_verbose = ChatOllama(model="llama3.1:8b", temperature=0, verbose=True)
llm_verbose.verbose=True
llm_with_tools = llm_verbose.bind_tools([multiply])

out = llm_with_tools.invoke("What is 2 times 3?")
print(vars(out))