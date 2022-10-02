class Constants:
    types = {
        "int": (0, "32-bit integer"),
        "boolean": (1, "boolean variable"),
        "long": (2, "64-bit integer"),
        "string": (3, "string of chars"),
    }

    operators = {
        "=": (0, "assign_operation"),
        "+": (1, "sum_operation"),
        "-": (2, "subtract_operation"),
        "*": (3, "multiply_operation"),
        "/": (4, "divide_operation"),
        "+=": (5, "add_amount_operation"),
        "-=": (6, "subtract_amount_operation"),
        "==": (7, "are_equal_operation"),
        ">": (8, "more_operation"),
        "<": (9, "less_operation"),
        "++": (10, "increment_operation"),
        "--": (11, "decrement_operation"),
        "%": (12, "modulo_operation"),
        "%=": (13, "modulo_amount_operation"),
        "*=": (14, "multiply_amount_operation"),
        "/=": (15, "divide_amount_operation"),
    }

    Keywords = {
        "class": (0, 'class'),
        "public": (1, 'public'),
        "private": (2, 'private'),
        "do": (3, 'do'),
        "return": (4, 'return'),
        "if": (5, 'if'),
        "else": (6, 'else'),
        "while": (7, 'while'),
        "false": (8, 'false'),
        "true": (9, 'true')
    }

    KeySymbols = {
        ".": (0, '.'),
        ";": (1, ';'),
        ",": (2, ','),
        "(": (3, '('),
        ")": (4, ')'),
        "[": (5, '['),
        "]": (6, ']'),
        "{": (7, '{'),
        "}": (8, '}')
    }
