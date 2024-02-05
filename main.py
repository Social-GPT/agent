from utils import create_directory
from generators.topic_generator import TopicGenerator
from generators.idea_generator import IdeaGenerator
from generators.tweet_generator import TweetGenerator
from generators.facebook_generator import FacebookGenerator
from generators.instagram_generator import InstagramGenerator
from generators.linkedin_generator import LinkedInGenerator
from generators.image_prompt_generator import ImagePromptGenerator
from generators.image_generator import generate_image_with_hf
from generators.unsplash_prompt_generator import UnsplashPromptGenerator
from generators.unsplash_grabber import fetch_and_save_images_from_unsplash
from utils import ask_boolean, prepare_directories
from brands import Brand
import os
import inquirer
from llm import LLM


def main():
    prepare_directories()

    brand = Brand.request_brand()
    topic_count = int(input("\nNumber of topics to generate?\n"))
    ideas_per_topic = int(input("\nNumber of posts per topic?\n"))
    posts_language = input("\nLanguage of the posts?\n")
    topics_ideas_prompt_expansion = input(
        "\nAny specific request about the TOPICS/IDEAS?\n") or ""
    posts_prompt_expansion = input(
        "\nAny specific request about the style or content of the POSTS?\n") or ""
    generate_images = ask_boolean(
        "\nUse image generation feature (beta)?", False)
    print("\n")
    platforms = inquirer.prompt([inquirer.Checkbox('platforms', message="Which platforms do you want to target?", choices=[
        "Instagram", "Facebook", "Twitter", "LinkedIn"])])['platforms']

    mode = LLM.request_generation_mode()

    print('\n👍🏼 Nice! Started generating...\n')

    topics = TopicGenerator(
        brand, topic_count, topics_ideas_prompt_expansion, mode).generate_topics()

    for topic in topics:
        ideas = IdeaGenerator(
            brand, ideas_per_topic, topics_ideas_prompt_expansion, mode).generate_ideas(topic)

        for idea in ideas:
            if "Twitter" in platforms:
                TweetGenerator(brand, posts_language, idea,
                               posts_prompt_expansion, mode).generate_tweet()
            if "Facebook" in platforms:
                FacebookGenerator(brand, posts_language, idea,
                                  posts_prompt_expansion, mode).generate_post()
            if "Instagram" in platforms:
                InstagramGenerator(brand, posts_language, idea,
                                   posts_prompt_expansion, mode).generate_post()
            if "LinkedIn" in platforms:
                LinkedInGenerator(brand, posts_language, idea,
                                  posts_prompt_expansion, mode).generate_post()
            if generate_images:
                hf_api_token = os.environ.get("HUGGINGFACE_API_TOKEN")
                if hf_api_token:
                    image_prompt = ImagePromptGenerator(
                        brand, idea, mode).generate_prompt()
                    generate_image_with_hf(image_prompt)
                else:
                    print("⚠️ Using Unsplash as you did not set the HUGGINGFACE_API_TOKEN environment variable for image generation.")
                    image_prompt = UnsplashPromptGenerator(
						brand, idea, mode).generate_prompt()
                    fetch_and_save_images_from_unsplash(image_prompt)
                    

    print('\n\n✅ Done!')


if __name__ == "__main__":
    main()
