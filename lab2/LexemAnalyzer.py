from Models.Word import Word


class LexemAnalyzer:
    Line = 1
    Peek = ' '
    keywords = {}
    Pointer = 0

    @staticmethod
    def reserve(word: Word):
        LexemAnalyzer.keywords[word.Lexeme] = word

    @staticmethod
    def programming(path):
        with open(path, 'r') as f:
            print(f.read())
