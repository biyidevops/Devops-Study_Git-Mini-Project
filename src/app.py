import logging

logging.basicConfig(level=logging.INFO)

def greet(name):
    return f"Hello {name}!"


if __name__ == "__main__":
    print(greet("DevOps Engineer"))
