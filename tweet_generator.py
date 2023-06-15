from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage, SystemMessage
from utils import format_list, write_to_file

class TweetGenerator:
    def __init__(self, brand_info, topic_count, ideas_per_topic):
        self.gpt3 = ChatOpenAI(temperature=0.5)
        self.gpt4 = ChatOpenAI(temperature=0.5, model_name="gpt-4")
        self.brand_info = brand_info
        self.topic_count = topic_count
        self.ideas_per_topic = ideas_per_topic

    def generate_topics(self):
        prompt = f"Create a list of {self.topic_count} general topics or fields to cover in their tweets, in the format '- Text of first topic....\n- Text of second...'"
        topics = [
            i.replace("- ", "")
            for i in self.gpt3([SystemMessage(content=self.brand_info), HumanMessage(content=prompt)])
            .content.strip()
            .split("\n")
            if len(i) > 2
        ]
        print('\n---------')
        print("\nGenerated topics:\n\n", format_list(topics), "\n\n---------\n")
        write_to_file("results/topics.txt", '\n'.join(topics))
        return topics

    def generate_ideas(self, topic):
        topic_prompt = f"Create a list of {self.ideas_per_topic} tweet ideas (concise and specific) for their account about the topic '{topic}' in the format '- Text for first idea....\n- Text of second...'"
        ideas = [
            i.replace("- ", "")
            for i in self.gpt3(
                [SystemMessage(content=self.brand_info), HumanMessage(content=topic_prompt)]
            )
            .content.strip()
            .split("\n")
            if len(i) > 2
        ]
        print("Generated ideas:\n\n", format_list(ideas), "\n\n---------\n")
        write_to_file("results/ideas.txt", '\n'.join(ideas), mode='a')
        return ideas

    def generate_tweets(self, idea):
        idea_prompt = f"Write a tweet for his account that talks about '{idea}'"
        tweet = self.gpt4(
            [SystemMessage(content=self.brand_info), HumanMessage(content=idea_prompt)]
        ).content.strip()
        print("Generated tweet:\n\n", tweet, "\n\n---------\n")
        write_to_file("results/tweets.txt", tweet, mode='a')
        return tweet
