#Added by Travis Peacock
from langchain_openai import ChatOpenAI
from langchain.schema import HumanMessage, SystemMessage
from brands import Brand
from llm import LLM, GenerationMode, GenerationItemType

class UnsplashPromptGenerator:
    def __init__(self, brand: Brand, post_idea: str, generation_mode: GenerationMode):
        self.brand = brand
        self.post_idea = post_idea
        self.generation_mode = generation_mode

    def generate_prompt(self):
        prompt = f"Based on the following post idea, define one single, broad term that represents a tangible place, object, or thing. The term should be broad, but not too broad. Like a state instead of a city, but not country or an animal instead of a breed of an animal but not just the word animal:\n\n'{self.post_idea}'\n\nNote: The result should be one word that captures the essence of the post idea in a general way but not too broad."
        unsplash_prompt = LLM.generate([SystemMessage(
            content=self.brand.description), HumanMessage(content=prompt)], GenerationItemType.IMAGE_PROMPT, self.generation_mode).content

        return unsplash_prompt
