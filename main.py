from utils import create_directory
from generators.topic_generator import TopicGenerator
from generators.idea_generator import IdeaGenerator
from generators.tweet_generator import TweetGenerator
from generators.facebook_generator import FacebookGenerator
from generators.instagram_generator import InstagramGenerator

def main():
    create_directory('results')

    topic_count = int(input("\nNumber of topics?\n"))
    ideas_per_topic = int(input("\nNumber of posts per topic?\n"))
    posts_language = input("\nLanguage of the posts?\n")
    brand_info = input("\nWrite a description of the brand:\n")

    topics = TopicGenerator(brand_info, topic_count).generate_topics()

    for topic in topics:
        ideas = IdeaGenerator(brand_info, ideas_per_topic).generate_ideas(topic)

        for idea in ideas:
            TweetGenerator(brand_info, posts_language, idea).generate_tweet()
            FacebookGenerator(brand_info, posts_language, idea).generate_post()
            InstagramGenerator(brand_info, posts_language, idea).generate_post()

if __name__ == "__main__":
    main()
