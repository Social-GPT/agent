from langchain_openai import ChatOpenAI
from langchain.schema import HumanMessage, SystemMessage
from utils import format_list, write_to_file
from brands import Brand
from prompts import Prompts
from llm import LLM
from logger import Logger
from files import Files
from llm import LLM, GenerationMode, GenerationItemType


class TopicGenerator:
    def __init__(self, brand: Brand, topic_count: str, prompt_expansion: str, generation_mode: GenerationMode):
        self.brand = brand
        self.prompt_expansion = prompt_expansion
        self.topic_count = topic_count
        self.generation_mode = generation_mode

    def generate_topics(self):
        prompt = f"Create a list of {self.topic_count} general topics or fields to cover in their social media posts, in the format '- ...\n- ...'{Prompts.get_avoids()}"
        if (self.prompt_expansion != ""):
            prompt = prompt + \
                f"\n\nTake this also into account: {self.prompt_expansion}"
        topics = [
            i.replace("- ", "")
            for i in LLM.generate([SystemMessage(content=self.brand.description), HumanMessage(content=prompt)], GenerationItemType.IDEAS, self.generation_mode)
            .content.strip()
            .split("\n")
            if len(i) > 2
        ][: self.topic_count]
        print('\n---------')
        Logger.log("Generated topics", format_list(topics))
        write_to_file(Files.topic_results, '\n'.join(topics))
        return topics
