from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage, SystemMessage

class ImagePromptGenerator:
    def __init__(self, brand_info, post_idea):
        self.gpt3 = ChatOpenAI(temperature=0.5)
        self.brand_info = brand_info
        self.post_idea = post_idea

    def generate_prompt(self):
        post_idea_prompt = f"Define with 10-20 words the description for the image that will be used for the following post idea:\n\n'{self.post_idea}'.\n\nNote: You should describe all the items we will see in the image, and those items should NOT include people's faces, hands, text or animals, device screens or anything that could contain text. Good examples to include would be common objects and scenes."
        image_prompt = self.gpt3([SystemMessage(content=self.brand_info), HumanMessage(content=post_idea_prompt)]).content
        prompt = """
        {}, rendered in a hyperrealistic style. Text is transparent and cannot be seen. Detailed, high-resolution textures, (detailed skin), and true-to-life color reproduction (grade:Kodak Ektar 100 film). Subtle lighting effects reminiscent of Gregory Crewdson's photography. An underlying surrealist ambiance inspired by Rene Magritte. Apply an ultra-wide lens effect with slight lens flare. Attention to minute detail - (Visible pores), (visible skin texture), (microscopic hair detail). High contrast, full dynamic range - 16k, UHD, HDR. The image should be as detailed and lifelike as possible. (Masterpiece:1.5), (highest quality:1.5), shot with a cinematic camera in a controlled studio environment.
        """.format(image_prompt)

        return prompt