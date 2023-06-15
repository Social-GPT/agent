# Social GPT

**Social GPT** is an **Open Source** tool designed to autonomously strategize and execute your social media campaign. Using the advanced capabilities of GPT-3 and GPT-4, this AI-driven solution is tailored to streamline your social media management efforts, allowing for effective and efficient engagement with your audience.

## 🤖 Why Social GPT?

In an era where social media is a cornerstone of digital marketing, Social GPT acts as your very own **social media strategist**. By leveraging AI technology, it not only optimizes your social media strategy but also executes it for you, saving you significant time and effort. It takes care of everything from post scheduling to hashtag strategy, all the while learning and adapting to your specific needs.

## ✅ Features

- 💡 Offers suggestions according to the provided brand description
- 📝 Generates a list of topics and formulates ideas for each one
- 🤖 Creates the body of posts automatically
- 🐦 Facilitates post creation for Twitter, 📘 Facebook, and 📸 Instagram
- 🎆 Generates images for each post using StableDiffusion
- 🔍 Selects hashtags intelligently
- 😊 Incorporates emojis in the posts
- 🌐 Allows you to write posts in any language

## 🗺️ Roadmap
- 🖼️ Plans to automatically select images from Unsplash
- 📣 Working on different brand communication styles
- 🕺 Aspires to incorporate Tiktok, 📌 Pinterest, 💼 LinkedIn, and more


## 🛑 Limitations

Although Social GPT is a potent tool, it's not a panacea for all social media challenges. It does have some limitations:

- 🔑 It necessitates an API key from OpenAI, which might entail associated costs.
- 📊 Its performance largely depends on the quality and quantity of data supplied for the brand description.
- 🧑‍💻 While it's designed to learn and adapt, human supervision is still advisable to guarantee the appropriateness and effectiveness of the content.

## 🙌🏼 Getting Started

To get started with Social GPT, you will need to follow the setup instructions as listed below:

**Prerequisites**

Ensure you have Python 3.6 or later installed on your system. If not, you can download it from [here](https://www.python.org/downloads/).

**Installation**

1. Clone this repository to your local machine.

```bash
git clone https://github.com/social-gpt/agent.git
```

2. Navigate to the cloned directory and install the required dependencies by executing the following command:

```bash
pip install -r requirements.txt
```

3. Set up your OpenAI API key. Make sure to replace `{your-api-key}` with your actual API key.

```bash
export OPENAI_API_KEY={your-api-key}
```

4. If you want Social-GPT to also generate images, set up your HuggingFace API key. Make sure to replace `{your-api-token}` with your actual API key.

```bash
export HUGGINGFACE_API_TOKEN={your-api-token}
```

**Usage**

After setting up, you can start using Social GPT by running the `main.py` file:

```bash
python main.py
```

## Contribution

Feel free to contribute to this project and help improve it. We are open to suggestions, bug reports, and pull requests. Please follow the contribution guidelines mentioned in the [CONTRIBUTING.md](https://githum.com/social-gpt/agent/CONTRIBUTING.md) file.

## License

This project is licensed under the MIT License. Please see the LICENSE file for more details.