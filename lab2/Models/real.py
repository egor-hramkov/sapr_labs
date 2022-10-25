from Models.token import Token


class Real(Token):
    Value = float()

    def __init__(self, value):
        self.Value = value

    def __str__(self):
        return print(f"{self.Value}")
