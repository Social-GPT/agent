from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage, SystemMessage
from utils import format_list, add_item_to_file

class IdeaGenerator:
    def __init__(self, brand_info, number_of_ideas):
        self.gpt3 = ChatOpenAI(temperature=0.5)
        self.gpt4 = ChatOpenAI(temperature=0.5, model_name="gpt-4")
        self.brand_info = brand_info
        self.number_of_ideas = number_of_ideas

    def generate_ideas(self, topic):
        topic_prompt = f"Create a list of {self.number_of_ideas} social media post ideas (concise and specific) for their account about the topic '{topic}' in the format '- ...\n- ...\n\nNote: avoid ideas that require up-to-date information, and avoid ideas that depend on a real link or offered product/service'"
        ideas = [
            i.replace("- ", "")
            for i in self.gpt3(
                [SystemMessage(content=self.brand_info), HumanMessage(content=topic_prompt)]
            )
            .content.strip()
            .split("\n")
            if len(i) > 2
        ][: self.number_of_ideas]
        print("Generated ideas:\n\n", format_list(ideas), "\n\n---------\n")
        for idea in ideas:
            add_item_to_file("results/ideas.txt", idea)
        return ideas
