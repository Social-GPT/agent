class Logger:
    def log(title: str, content: str):
        print(f"\033[1;32;40m{title}\033[0m\n\n{content}\n\n---------\n")
