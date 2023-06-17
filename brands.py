from utils import add_item_to_file, ask_boolean

class Brand:

    def __init__(self, title, description):
        self.title = title
        self.description = description

    @staticmethod
    def from_cache_text(text):
        title = text.split(" - ")[0]
        description = text.split(" - ")[1]
        return Brand(title, description)
    
    def to_cache_text(self):
        return f"{self.title} - {self.description}"
    
    @staticmethod
    def create_new_brand():
        name = input("\nWhich is the name of the brand?\n")
        description = input("\nWrite a description for the brand:\n")
        add_item_to_file("cache/brands", Brand(name, description).to_cache_text())
        return Brand(name, description)

    
    @staticmethod
    def request_brand_info():
        cached = Brand.get_cached_brands()
        if (len(cached) == 0):
           return  Brand.create_new_brand()
        else:
            print("\nSelect a saved brand:")
            for brand in cached:
                print(brand.title)
            print(f"{len(cached)+1}. Write a new brand")
            option = int(input())
            if option == len(cached)+1:
                return Brand.create_new_brand()
            else:
                return cached[option-1]

    @staticmethod
    def get_cached_brands():
        with open("cache/brands", 'r') as f:
            brand_texts = []
            last_line = ""
            for line in f:
                if line.strip() == "---":
                    brand_texts.append(last_line)
                    last_line = ""
                else:
                    last_line += line.strip()
        return [Brand.from_cache_text(brand_text) for brand_text in brand_texts]

    def save_in_cache(self):
        add_item_to_file("cache/brands", self.to_cache_text())