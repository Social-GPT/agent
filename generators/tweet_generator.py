from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage, SystemMessage
from utils import format_list, write_to_file

class TweetGenerator:
    def __init__(self, brand_info, language, idea):
        self.gpt3 = ChatOpenAI(temperature=0.5)
        self.gpt4 = ChatOpenAI(temperature=0.5, model_name="gpt-4")
        self.brand_info = brand_info
        self.language = language
        self.idea = idea

    def generate_tweet(self):
        idea_prompt = f"Write a tweet in {self.language} for their account that talks about '{self.idea}'"
        tweet = self.gpt4(
            [SystemMessage(content=self.brand_info), HumanMessage(content=idea_prompt)]
        ).content.strip()
        print("Generated tweet:\n\n", tweet, "\n\n---------\n")
        write_to_file("results/tweets.txt", tweet, mode='a')
        return tweet
