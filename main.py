from utils import create_directory
from generators.topic_generator import TopicGenerator
from generators.idea_generator import IdeaGenerator
from generators.tweet_generator import TweetGenerator
from generators.facebook_generator import FacebookGenerator
from generators.instagram_generator import InstagramGenerator
from generators.image_prompt_generator import ImagePromptGenerator
from generators.image_generator import generate_image_with_hf
import os

def main():
    create_directory('results')
    create_directory('results/images')

    topic_count = int(input("\nNumber of topics?\n"))
    ideas_per_topic = int(input("\nNumber of posts per topic?\n"))
    posts_language = input("\nLanguage of the posts?\n")
    brand_info = input("\nWrite a description of the brand:\n")

    print('\👍🏼 nNice! Started generating...\n')

    topics = TopicGenerator(brand_info, topic_count).generate_topics()

    for topic in topics:
        ideas = IdeaGenerator(brand_info, ideas_per_topic).generate_ideas(topic)

        for idea in ideas:
            TweetGenerator(brand_info, posts_language, idea).generate_tweet()
            FacebookGenerator(brand_info, posts_language, idea).generate_post()
            InstagramGenerator(brand_info, posts_language, idea).generate_post()
            
            hf_api_token = os.environ.get("HUGGINGFACE_API_TOKEN")
            if hf_api_token:
                image_prompt = ImagePromptGenerator(brand_info, idea).generate_prompt()
                generate_image_with_hf(image_prompt)
                
    print('\n\n✅ Done!')

if __name__ == "__main__":
    main()
