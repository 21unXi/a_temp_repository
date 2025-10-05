def hello_world():
    print("Hello, World! This is a very long line that exceeds the typical "
          "79-character limit recommended by PEP8, so we can see flake8 "
          "complain about it.")
    x = 5
    y = 10
    if x < y:
        print("x is less than y")


class MyClass:
    def __init__(self):
        self.data = []
