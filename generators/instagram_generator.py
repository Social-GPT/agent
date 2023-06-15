from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage, SystemMessage
from utils import add_item_to_file

class InstagramGenerator:
    def __init__(self, brand_info, language, idea):
        self.gpt3 = ChatOpenAI(temperature=0.5)
        self.gpt4 = ChatOpenAI(temperature=0.5, model_name="gpt-4")
        self.brand_info = brand_info
        self.language = language
        self.idea = idea

    def generate_post(self):
        idea_prompt = f"Write an Instagram post in {self.language} for his account that talks about '{self.idea}'. \n\nNote: avoid including any text which requires up-to-date information, or which mentions a real link or offered product/service"
        post = self.gpt4(
            [SystemMessage(content=self.brand_info), HumanMessage(content=idea_prompt)]
        ).content.strip()
        print("Generated Instagram post:\n\n", post, "\n\n---------\n")
        add_item_to_file("results/instagram.txt", post)
        return post
