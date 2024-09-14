
from langchain_community.llms import Ollama
from time import sleep

llm = Ollama(model = "llama3")

res = llm.invoke(input(">> "))

for letters in range(len("llama3")) :
    print(res[letters],end= "", flush = True)
    sleep(0.1)
