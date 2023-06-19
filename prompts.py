from style import default_writting_style_definitions
from brands import Brand

class Prompts: 
    
    @staticmethod
    def get_avoids():
        return "\n\nNote: avoid including any text or ideas which requires up-to-date information, or which could contain false data, or which mentions a real link or offered product/service"
    
    def build_style_prompt(style_items: str):
        return '\n\nFollow these style guidelines:' + ', '.join(style_items)