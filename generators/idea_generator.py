from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage, SystemMessage
from utils import format_list, add_item_to_file
from prompts import Prompts
from files import Files
from brands import Brand
from logger import Logger
from llm import LLM, GenerationMode, GenerationItemType


class IdeaGenerator:
    def __init__(self, brand: Brand, number_of_ideas: str, prompt_expansion: str, generation_mode: GenerationMode):
        self.brand = brand
        self.number_of_ideas = number_of_ideas
        self.prompt_expansion = prompt_expansion
        self.generation_mode = generation_mode

    def generate_ideas(self, topic):
        prompt = f"Create a list of {self.number_of_ideas} social media post ideas (concise and specific) for their account about the topic '{topic}' in the format '- ...\n- ...'{Prompts.get_avoids()}"
        if (self.prompt_expansion != ""):
            prompt = prompt + \
                f"\n\nTake this also into account: {self.prompt_expansion}"
        ideas = [
            i.replace("- ", "")
            for i in LLM.generate(
                [SystemMessage(content=self.brand.description), HumanMessage(
                    content=prompt)], GenerationItemType.IDEAS, self.generation_mode
            )
            .content.strip()
            .split("\n")
            if len(i) > 2
        ][: self.number_of_ideas]
        Logger.log("Generated ideas", format_list(ideas))
        for idea in ideas:
            add_item_to_file(Files.idea_results, idea)
        return ideas
