from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage, SystemMessage
from utils import add_item_to_file

class TweetGenerator:
    def __init__(self, brand_info, language, idea, prompt_expansion):
        self.gpt3 = ChatOpenAI(temperature=0.5)
        self.gpt4 = ChatOpenAI(temperature=0.5, model_name="gpt-4")
        self.brand_info = brand_info
        self.language = language
        self.idea = idea
        self.prompt_expansion = prompt_expansion

    def generate_tweet(self):
        idea_prompt = f"Write a tweet in {self.language} for their account that talks about '{self.idea}'\n\nNote: avoid including any text which requires up-to-date information, or which mentions a real link or offered product/service\n\nTake this also into account: {self.prompt_expansion}"
        tweet = self.gpt4(
            [SystemMessage(content=self.brand_info), HumanMessage(content=idea_prompt)]
        ).content.strip()
        print("Generated tweet:\n\n", tweet, "\n\n---------\n")
        add_item_to_file("results/tweets.txt", tweet)
        return tweet
