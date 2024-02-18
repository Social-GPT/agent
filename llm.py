from langchain_openai import ChatOpenAI
from enum import Enum
import inquirer


class GenerationItemType(Enum):
    TOPICS = 1
    IDEAS = 2
    POST = 3
    IMAGE_PROMPT = 4


class GenerationMode(Enum):
    LOW = 1
    MEDIUM = 2
    HIGH = 3

    def to_string(self):
        if self == GenerationMode.LOW:
            return "Low quality (fast + cheap)"
        if self == GenerationMode.MEDIUM:
            return "Medium quality (recommended)"
        if self == GenerationMode.HIGH:
            return "High quality (slow + expensive)"

    def get_mode_strings():
        return [
            GenerationMode.LOW.to_string(),
            GenerationMode.MEDIUM.to_string(),
            GenerationMode.HIGH.to_string(),
        ]

    @staticmethod
    def from_string(value: str):
        if value == "Low quality (fast + cheap)":
            return GenerationMode.LOW
        if value == "Medium quality (recommended)":
            return GenerationMode.MEDIUM
        if value == "High quality (slow + expensive)":
            return GenerationMode.HIGH


class LLM:

    gpt3 = ChatOpenAI(temperature=0.5, model="gpt-3.5-turbo")
    gpt4 = ChatOpenAI(temperature=0.5, model="gpt-4")

    @staticmethod
    def generate(prompt: str, type: GenerationItemType, mode: GenerationMode):
        if type == GenerationItemType.TOPICS:
            if mode == GenerationMode.HIGH:
                return LLM.gpt4(prompt)
            else:
                return LLM.gpt3(prompt)
        if type == GenerationItemType.IDEAS:
            if mode == GenerationMode.HIGH:
                return LLM.gpt4(prompt)
            else:
                return LLM.gpt3(prompt)
        if type == GenerationItemType.POST:
            if mode == GenerationMode.LOW:
                return LLM.gpt3(prompt)
            else:
                return LLM.gpt4(prompt)
        if type == GenerationItemType.IMAGE_PROMPT:
            if mode == GenerationMode.HIGH:
                return LLM.gpt4(prompt)
            else:
                return LLM.gpt3(prompt)

    @staticmethod
    def request_generation_mode():
        return GenerationMode.from_string(inquirer.prompt([inquirer.List(
            'generation', message="Which generation mode will be used?", choices=GenerationMode.get_mode_strings(), default=GenerationMode.MEDIUM.to_string())])['generation'])
