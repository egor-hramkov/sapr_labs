class Lexem:
    
    type = ""
    id = ""
    value = ""

    def __init__(self, _type, _id, _value):
        self.type = _type
        self.id = _id
        self.value = _value

    def ToString(self):
        return f"lexem type: {self.type};\t lexem id: {self.id};\t value: {self.value}"