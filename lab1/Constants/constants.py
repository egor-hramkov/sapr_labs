class Constants:
    types = {
        {"int": (0, "32-bit integer")},
        {"boolean": (1, "boolean variable")},
        {"long": (2, "64-bit integer")},
        {"string": (3, "string of chars")},
    }

    operators = {
        {"=": (0, "assign_operation")},
        {"+": (1, "sum_operation")},
        {"-": (2, "subtract_operation")},
        {"*": (3, "multiply_operation")},
        {"/": (4, "divide_operation")},
        {"+=": (5, "add_amount_operation")},
        {"-=": (6, "subtract_amount_operation")},
        {"==": (7, "are_equal_operation")},
        {">": (8, "more_operation")},
        {"<": (9, "less_operation")},
        {"++": (10, "increment_operation")},
        {"--": (11, "decrement_operation")},
        {"%": (12, "modulo_operation")},
    }

    Keywords = ["class", "public", "private", "do", "return", "if", "else", "while"]

    KeySymbols = [".", ";", ",", "(", ")", "[", "]", "{", "}"]
