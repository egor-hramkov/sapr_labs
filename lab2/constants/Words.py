from Models.Word import Word
from constants.tags import Tags


class Words:
    And = Word("&&", Tags['And'])
    Or = Word("||", Tags['Or'])
    Eq = Word("==", Tags['Eq'])
    Ne = Word("!=", Tags['Ne'])
    Le = Word("<=", Tags['Le'])
    Ge = Word(">=", Tags['Ge'])
    Minus = Word("minus", Tags['Minus'])
    true = Word("true", Tags['True'])
    false = Word("false", Tags['False'])
    Temp = Word("t", Tags['Temp'])

