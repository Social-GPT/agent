from utils import create_directory
from tweet_generator import TweetGenerator

def main():
    create_directory('results')

    topic_count = int(input("\nNumber of topics?\n"))
    ideas_per_topic = int(input("\nNumber of posts per topic?\n"))
    brand_info = input("\nWrite a description of the brand:\n")

    generator = TweetGenerator(brand_info, topic_count, ideas_per_topic)
    topics = generator.generate_topics()

    for topic in topics:
        ideas = generator.generate_ideas(topic)
        for idea in ideas:
            generator.generate_tweets(idea)

if __name__ == "__main__":
    main()
