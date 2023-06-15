from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage, SystemMessage
import os

def create_directory(dir: str):
    if not os.path.exists(dir):
        os.makedirs(dir)

def format_list(items):
    return "\n".join([f"- {item}" for item in items])


def main():
    create_directory('results')
    topic_count = int(input("Number of topics?\n"))
    ideas_per_topic = int(input("Number of ideas per topic?\n"))
    brand_info = input("Write a description of the brand:\n")

    gpt3 = ChatOpenAI(temperature=0.5)
    gpt4 = ChatOpenAI(temperature=0.5, model_name="gpt-4")

    prompt = f"Create a list of {topic_count} general topics or fields to cover in their tweets, in the format '- Text of first topic....\n- Text of second...'"
    topics = [
        i.replace("- ", "")
        for i in gpt3([SystemMessage(content=brand_info), HumanMessage(content=prompt)])
        .content.strip()
        .split("\n")
        if len(i) > 2
    ]
    print("Generated topics:\n", format_list(topics), "\n\n")

    with open("results/topics.txt", "a") as f:
        for topic in topics:
            f.write(topic + "\n")

    results = []

    for topic in topics:
        topic_prompt = f"Create a list of {ideas_per_topic} tweet ideas (concise and specific) for their account about the topic '{topic}' in the format '- Text for first idea....\n- Text of second...'"
        ideas = [
            i.replace("- ", "")
            for i in gpt3(
                [SystemMessage(content=brand_info), HumanMessage(content=topic_prompt)]
            )
            .content.strip()
            .split("\n")
            if len(i) > 2
        ]
        print("Generated ideas:\n", format_list(ideas), "\n\n")

        for idea in ideas:
            with open("results/ideas.txt", "w") as f:
                f.write(idea + "\n")
            idea_prompt = f"Write a tweet for his account that talks about '{idea}'"
            tweet = gpt4(
                [SystemMessage(content=brand_info), HumanMessage(content=idea_prompt)]
            ).content.strip()
            results.append(tweet)
            print("Generated tweet: ", tweet, "\n\n")
            with open("results/tweets.txt", "a") as f:
                f.write(tweet + "\n")


if __name__ == "__main__":
    main()
