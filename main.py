from utils import create_directory
from generators.topic_generator import TopicGenerator
from generators.idea_generator import IdeaGenerator
from generators.tweet_generator import TweetGenerator
from generators.facebook_generator import FacebookGenerator
from generators.instagram_generator import InstagramGenerator
from generators.image_prompt_generator import ImagePromptGenerator
from generators.image_generator import generate_image_with_hf
from utils import ask_boolean, prepare_directories
from brands import Brand
import os
import inquirer

def main():
    prepare_directories()

    topic_count = int(input("\nNumber of topics?\n"))
    ideas_per_topic = int(input("\nNumber of posts per topic?\n"))
    posts_language = input("\nLanguage of the posts?\n")
    brand_info = Brand.request_brand_info().description
    topics_ideas_prompt_expansion = input("\nAny specific request about the TOPICS/IDEAS?\n")
    posts_prompt_expansion = input("\nAny specific request about the style or content of the POSTS?\n")
    generate_images = ask_boolean("\nUse image generation feature (beta)?", False)
    platforms = inquirer.prompt([inquirer.Checkbox('platforms', message="\nWhich platforms do you want to target??", choices=["Instagram", "Facebook", "Twitter"])])

    print('\n👍🏼 Nice! Started generating...\n')

    topics = TopicGenerator(brand_info, topic_count).generate_topics(topics_ideas_prompt_expansion)

        

    for topic in topics:
        ideas = IdeaGenerator(brand_info, ideas_per_topic).generate_ideas(topic, topics_ideas_prompt_expansion)

        for idea in ideas:
            if "Twitter" in platforms:
                TweetGenerator(brand_info, posts_language, idea).generate_tweet(posts_prompt_expansion)
            if "Facebook" in platforms:
                FacebookGenerator(brand_info, posts_language, idea).generate_post(posts_prompt_expansion)
            if "Instagram" in platforms:
                InstagramGenerator(brand_info, posts_language, idea).generate_post(posts_prompt_expansion)            
            if generate_images:
                hf_api_token = os.environ.get("HUGGINGFACE_API_TOKEN")
                if hf_api_token:
                    image_prompt = ImagePromptGenerator(brand_info, idea).generate_prompt()
                    generate_image_with_hf(image_prompt)

    print('\n\n✅ Done!')

if __name__ == "__main__":
    main()