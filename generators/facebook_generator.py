from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage, SystemMessage
from utils import add_item_to_file
from prompts import Prompts

class FacebookGenerator:
    def __init__(self, brand_info, language, idea, prompt_expansion):
        self.gpt3 = ChatOpenAI(temperature=0.5)
        self.brand_info = brand_info
        self.language = language
        self.idea = idea
        self.prompt_expansion = prompt_expansion

    def generate_post(self):
        idea_prompt = f"Write a facebook post with 3-6 paragraphs in {self.language} for his account that talks about '{self.idea}'{Prompts.get_avoids()}{Prompts.get_default_style()}"
        if (self.prompt_expansion != ""):
            prompt = prompt + f"\n\nTake this also into account: {self.prompt_expansion}"
        post = self.gpt3(
            [SystemMessage(content=self.brand_info), HumanMessage(content=idea_prompt)]
        ).content.strip()
        print("Generated Facebook post:\n\n", post, "\n\n---------\n")
        add_item_to_file("results/facebook.txt", post)
        return post
