import requests
import os
import io
from PIL import Image
from logger import Logger
from utils import count_files_in_directory, retry_n_times

def fetch_and_save_images_from_unsplash(prompt: str, num_results: int = 1, retry_attempts: int = 3) -> list:
    API_URL = f"https://unsplash.com/napi/search/photos?per_page=20&query={prompt}"
    
    def request_to_unsplash():
        for attempt in range(retry_attempts):
            response = requests.get(API_URL)
            if response.ok:
                data = response.json()
                non_premium_images = [result for result in data['results'] if not result.get('premium', False)]
                if not non_premium_images:
                    print("No non-premium images found.")
                    return []
                filenames = []
                for image_data in non_premium_images[:num_results]:
                    image_url = image_data['urls']['regular']
                    try:
                        image_response = requests.get(image_url)
                        if image_response.ok:
                            image = Image.open(io.BytesIO(image_response.content))
                            existing_images = count_files_in_directory("results/images")
                            filename = f"post_{existing_images + 1}.jpg"  # Save as .jpg
                            image.save(f"results/images/{filename}")
                            Logger.log(f"Generated Image", f"Filename: {filename}\nPrompt: {prompt}")
                            filenames.append(filename)
                        else:
                            print(f"Failed to download image: {image_response.text}")
                    except Exception as e:
                        print(f"Error saving image: {e}")
                return filenames
            else:
                print(f"Failed to fetch images: {response.text}")
                if attempt < retry_attempts - 1:
                    print(f"Retrying... Attempt {attempt + 2}/{retry_attempts}")
                else:
                    print("All retry attempts failed.")
        return []

    return retry_n_times(retry_attempts, request_to_unsplash)

# Helper function for retry logic (adapt or implement as needed)
def retry_n_times(attempts, func, *args, **kwargs):
    for _ in range(attempts):
        result = func(*args, **kwargs)
        if result:
            return result
    return []

# Ensure the results/images directory exists
if not os.path.exists("results/images"):
    os.makedirs("results/images")