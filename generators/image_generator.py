""" Image Generation Module for AutoGPT."""
import io
import json
import time
from utils import retry_n_times, count_files_in_directory

import requests
from PIL import Image
import os
from logger import Logger


def generate_image_with_hf(prompt: str) -> str:
    hf_api_token = os.environ.get("HUGGINGFACE_API_TOKEN")
    if hf_api_token is None:
        raise ValueError(
            "You need to export HUGGINGFACE_API_TOKEN in your environment."
        )
    API_URL = f"https://api-inference.huggingface.co/models/CompVis/stable-diffusion-v1-4"
    headers = {
        "Authorization": f"Bearer {hf_api_token}",
        "X-Use-Cache": "false",
    }

    def request_to_hf():
        response = requests.post(
            API_URL,
            headers=headers,
            json={
                "inputs": prompt,
            },
        )

        if response.ok:
            try:
                image = Image.open(io.BytesIO(response.content))
                existing_images = count_files_in_directory("results/images")
                filename = f"post_{existing_images + 1}.png"
                Logger.log(f"Generated Image",
                           "Filename: {filename}\nPrompt: {prompt}")
                image.save(f"results/images/{filename}")
                return filename
            except Exception as e:
                print(e)
        else:
            try:
                error = json.loads(response.text)
                if "estimated_time" in error:
                    delay = error["estimated_time"]
                    print(response.text)
                    print("Retrying in", delay)
                    time.sleep(delay)
                else:
                    print(response.text)

            except Exception as e:
                print(e)

    retry_n_times(3, request_to_hf)
