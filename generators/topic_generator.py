from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage, SystemMessage
from utils import format_list, write_to_file

class TopicGenerator:
    def __init__(self, brand_info, topic_count, prompt_expansion):
        self.gpt3 = ChatOpenAI(temperature=0.5)
        self.brand_info = brand_info
        self.prompt_expansion = prompt_expansion

        self.topic_count = topic_count

    def generate_topics(self):
        prompt = f"Create a list of {self.topic_count} general topics or fields to cover in their social media posts, in the format '- ...\n- ...\n\nNote: avoid any topic that would require up-to-date information'"
        if (self.prompt_expansion != ""):
            prompt = prompt + f"\n\nTake this also into account: {self.prompt_expansion}"
        topics = [
            i.replace("- ", "")
            for i in self.gpt3([SystemMessage(content=self.brand_info), HumanMessage(content=prompt)])
            .content.strip()
            .split("\n")
            if len(i) > 2
        ][: self.topic_count]
        print('\n---------')
        print("\nGenerated topics:\n\n", format_list(topics), "\n\n---------\n")
        write_to_file("results/topics.txt", '\n'.join(topics))
        return topics