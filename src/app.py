import logging

logging.basicConfig(level=logging.INFO)

def greet(name):
    message = f"Hello {name}!"
    logging.info(f"Greeting generated: {message}")
    return message


if __name__ == "__main__":
    print(greet("DevOps Engineer"))
