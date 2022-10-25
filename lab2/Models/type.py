from Models.Word import Word


class DataType(Word):
    Width = 0

    def __init__(self, lexeme, tag, width):
        self.Width = width
