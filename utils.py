import os

def create_directory(dir: str):
    if not os.path.exists(dir):
        os.makedirs(dir)

def format_list(items):
    return "\n".join([f"- {item}" for item in items])

def write_to_file(filename, content, mode='w'):
    with open(filename, mode) as f:
        f.write(content + "\n")
