from Models.type import DataType
from constants.tags import Tags


class DataTypes:
    Int = DataType("int", Tags['Basic'], 4)
    Float = DataType("float", Tags['Basic'], 8)
    Char = DataType("char", Tags['Basic'], 1)
    Boolean = DataType("bool", Tags['Basic'], 1)
    Array = DataType("arr", Tags['Basic'], 1)
