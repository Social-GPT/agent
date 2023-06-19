from langchain.chat_models import ChatOpenAI
from brands import Brand

class LLM: 
    
    gpt3 = ChatOpenAI(temperature=0.5)

    @staticmethod
    def generate(prompt: str):
        return LLM.gpt3(prompt)
        