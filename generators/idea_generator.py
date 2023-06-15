from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage, SystemMessage
from utils import format_list, write_to_file

class IdeaGenerator:
    def __init__(self, brand_info, ideas_per_topic):
        self.gpt3 = ChatOpenAI(temperature=0.5)
        self.gpt4 = ChatOpenAI(temperature=0.5, model_name="gpt-4")
        self.brand_info = brand_info
        self.ideas_per_topic = ideas_per_topic

    def generate_ideas(self, topic):
        topic_prompt = f"Create a list of {self.ideas_per_topic} social media post ideas (concise and specific) for their account about the topic '{topic}' in the format '- Text for first idea....\n- Text of second...'"
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
