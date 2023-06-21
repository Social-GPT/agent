from langchain.schema import HumanMessage, SystemMessage
from utils import format_list, add_item_to_file
from prompts import Prompts
from files import Files
from brands import Brand
from logger import Logger
from llm import LLM, GenerationMode, GenerationItemType
from search.news import search_news_about

MAX_NEWS_POSTS = 5


class IdeaGenerator:
    def __init__(self, brand: Brand, number_of_ideas: str, prompt_expansion: str, generation_mode: GenerationMode, platforms):
        self.brand = brand
        self.number_of_ideas = number_of_ideas
        self.prompt_expansion = prompt_expansion
        self.generation_mode = generation_mode
        self.platforms = platforms

    def generate_default_ideas(self, topic: str, count: int):
        prompt = f"Create a list of {count} social media post ideas for their account about the topic '{topic}' in the format '- ...\n- ...'{Prompts.get_avoids()}"
        if (self.prompt_expansion != ""):
            prompt = prompt + \
                f"\n\nTake this also into account: {self.prompt_expansion}"
        result = LLM.generate(
            [SystemMessage(content=self.brand.description), HumanMessage(
                content=prompt)], GenerationItemType.IDEAS, self.generation_mode
        ).content.strip()
        return [
            i.replace("- ", "")
            for i in result.split("\n")
            if len(i) > 2
        ][: count]

    def generate_ideas_based_on_news(self, topic: str, count: int):
        news_search = search_news_about(topic, count)
        return [item['content'] for item in news_search]

    def generate_ideas(self, topic, use_news: bool):
        news_posts_count = min(
            int(self.number_of_ideas / 2), MAX_NEWS_POSTS) if use_news else 0
        ideas = []
        ideas.extend(self.generate_default_ideas(
            topic, self.number_of_ideas - news_posts_count))
        if (news_posts_count > 0):
            ideas.extend(self.generate_ideas_based_on_news(
                topic, news_posts_count))

        Logger.log("Generated ideas", format_list(ideas))
        for idea in ideas:
            add_item_to_file(Files.idea_results, idea)
        return ideas
