from utils import add_item_to_file, ask_boolean
import inquirer
from style import writting_style_definitions, default_writting_style_definitions
from files import Files


class Brand:

    def __init__(self, title, description, style):
        self.title = title
        self.description = description
        self.style = style

    @staticmethod
    def split_file_text(text):
        title = text.split(" - ")[0].split('. ')[1]
        content = text.split(" - ")[1]
        return [title, content]

    def to_description_cache_text(self):
        return f"{self.title} - {self.description}"

    def to_style_cache_text(self):
        return f"{self.title} - {', '.join(self.style)}"

    @staticmethod
    def from_title(title: str):
        brands = Brand.get_cached_brands()
        for brand in brands:
            if brand.title == title:
                return brand

    @staticmethod
    def create_new_brand():
        title = input("\nWhich is the name of the brand?\n")
        description = input("\nWrite a description for the brand:\n")
        print("\n")
        style = inquirer.prompt([inquirer.Checkbox('style', message="Select the style definitions for this brand",
                                choices=writting_style_definitions, default=default_writting_style_definitions)])['style']
        brand = Brand(title, description, style)
        add_item_to_file(Files.brand_descriptions,
                         brand.to_description_cache_text())
        add_item_to_file(Files.brand_styles, brand.to_style_cache_text())
        return Brand(title, description, style)

    @staticmethod
    def parse_brand_file(file: str):
        with open(file, 'r') as f:
            brand_texts = []
            last_line = ""
            for line in f:
                if line.strip() == "---":
                    brand_texts.append(last_line)
                    last_line = ""
                else:
                    last_line += line.strip()
        mapped_brands = {}
        for brand_text in brand_texts:
            [title, content] = Brand.split_file_text(brand_text)
            mapped_brands[title] = content
        return mapped_brands

    @staticmethod
    def request_brand():
        cached_brands = Brand.get_cached_brands()
        if (len(cached_brands) == 0):
            return Brand.create_new_brand()
        else:
            print("\n")
            brands = [brand.title for brand in cached_brands]
            brands.append("Create new brand")
            print("For which brand should I create the posts?")
            brand = inquirer.prompt(
                [inquirer.List('brand', choices=brands)])['brand']
            if brand == "Create new brand":
                return Brand.create_new_brand()
            else:
                return Brand.from_title(brand)

    @staticmethod
    def get_cached_brands():
        descriptions_map = Brand.parse_brand_file(Files.brand_descriptions)
        styles_map = Brand.parse_brand_file(Files.brand_styles)

        brands = []
        for brand in descriptions_map:
            brand = Brand(
                brand, descriptions_map[brand], styles_map[brand].split(', '))
            brands.append(brand)
        return brands

    def save_in_cache(self):
        add_item_to_file(Files.brand_descriptions,
                         self.to_description_cache_text())
        add_item_to_file(Files.brand_styles, self.to_style_cache_text())
