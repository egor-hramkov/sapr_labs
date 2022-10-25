from Models.type import DataType


class ArrayType(DataType):
    Of = DataType
    Size = 1

    def __init__(self, size, type):
        self.Size = size
        self.Of = type

    def __str__(self):
        return print(f"[{self.Size}] {self.Of}")
