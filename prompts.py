from style import default_writting_style_definitions

class Prompts: 
    
    @staticmethod
    def get_avoids():
        return "\n\nNote: avoid including any text or ideas which requires up-to-date information, or which could contain false data, or which mentions a real link or offered product/service"
    
    def get_default_style():
        return '\n\nFollow these style guidelines:' + ', '.join(default_writting_style_definitions)