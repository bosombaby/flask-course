import os


def sayhello(to=None):
    if to:
        return f"Hello, {to}!"
    return "Hello!"


SECRET_KEY = "1111"
print(dict(title="New Movie", year="2019"))
print(os.getenv("SECRET_KEY"))
