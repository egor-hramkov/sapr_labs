class Lexem:
    
    type = ""
    lex = ""
    value = ""

    def __init__(self, _type, _lex, _value):
        self.type = _type
        self.lex = _lex
        self.value = _value

    def ToString(self):
        return print(f"lexem type: {self.type};\t lexem id: {self.lex};\t value: {self.value}")