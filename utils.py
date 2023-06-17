import os

def create_directory(dir: str):
    if not os.path.exists(dir):
        os.makedirs(dir)

def ensure_file_created(filename: str):
    if not os.path.exists(filename):
        write_to_file(filename, "")

def format_list(items):
    return "\n".join([f"- {item}" for item in items])

def write_to_file(filename, content, mode='w'):
    with open(filename, mode) as f:
        f.write(content + "\n")

def retry_n_times(times, function):
    retry_count = 0
    result = None
    while result == None and retry_count < times:
        if retry_count > 0: 
            print(f"Retrying: {retry_count}")
        try:
            result = function()
        except Exception as e:
            print(e)
        retry_count += 1
    return None

def count_separators_in_file(filename, separator):
    try:
        count = 0
        if not os.path.exists(filename):
            write_to_file(filename, "")
        with open(filename, 'r') as f:
            for line in f:
                count += line.count(separator)
        return count
    except FileNotFoundError:
        print(f"File not found: {filename}")
        return 0
    except Exception as e:
        print(f"An error occurred: {e}")
        return 0

def add_item_to_file(filename, item):
    item_separator = "---"
    ensure_file_created(filename)
    position = count_separators_in_file(filename, item_separator) + 1
    write_to_file(filename, f"\n{position}. {item}\n\n{item_separator}", mode="a")

def count_files_in_directory(directory):
    try:
        files = os.listdir(directory)
        return len(files)
    except FileNotFoundError:
        print(f"Directory not found: {directory}")
        return 0
    except NotADirectoryError:
        print(f"Not a directory: {directory}")
        return 0
    except Exception as e:
        print(f"An error occurred: {e}")
        return 0

def ask_boolean(message: str, default: bool):
    if default == True:
        answer = input(f"{message} (Y/n)\n")
    else:
        answer = input(f"{message} (y/N)\n")
    return answer.lower() in ["y", "yes"] or (default == True and answer == "")

def prepare_directories():
    create_directory('results')
    create_directory('cache')
    ensure_file_created('cache/brands')
    create_directory('results/images')