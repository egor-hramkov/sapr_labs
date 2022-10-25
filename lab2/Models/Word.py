from Models.token import Token
class Word(Token):
    Lexeme = ""

    def __init__(self, lexeme, token: Token):
        self.Lexeme = lexeme

    def __str__(self):
        return print(self.Lexeme)