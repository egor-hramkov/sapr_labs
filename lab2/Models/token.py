class Token:
    Tag = int()

    def __init__(self, tag):
        self.Tag = tag

    def __str__(self):
        return print(f"{self.Tag}")
