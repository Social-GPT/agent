from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage, SystemMessage
from utils import write_to_file

class FacebookGenerator:
    def __init__(self, brand_info, language, idea):
        self.gpt3 = ChatOpenAI(temperature=0.5)
        self.gpt4 = ChatOpenAI(temperature=0.5, model_name="gpt-4")
        self.brand_info = brand_info
        self.language = language
        self.idea = idea

    def generate_post(self):
        idea_prompt = f"Write a facebook post in {self.language} for his account that talks about '{self.idea}'"
        post = self.gpt4(
            [SystemMessage(content=self.brand_info), HumanMessage(content=idea_prompt)]
        ).content.strip()
        print("Generated Facebook post:\n\n", post, "\n\n---------\n")
        write_to_file("results/facebook.txt", post, mode='a')
        return post
