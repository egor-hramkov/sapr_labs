from Models.token import Token


class Num(Token):
    Value = int()

    def __init__(self, val):
        self.Value = val

    def __str__(self):
        return print(f"{self.Value}")
