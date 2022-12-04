import os
from LexemProcessor import LexemProcessor


class Node:
    def __init__(self, node_name=None, value=None, type=None, v_name=None):
        self.node_name = node_name
        self.value = value
        self.type = type
        self.v_name = v_name


class Parser:
    main_str = ""

    @staticmethod
    def make_tree(path):
        if os.path.exists(path):
            if os.stat(path).st_size != 0:
                with open(path, "r") as f:
                    Parser.main_str = f.read()
                    lexs = Parser.main_str.split("\n")

                branch = ""

                with open("tree.txt", "w") as f:
                    print(lexs)
                    for i, l in enumerate(lexs):
                        if l != "":
                            temp_lex = l.split(";")
                            if temp_lex[0] == "Variable":
                                n = Node(temp_lex[0], temp_lex[1], temp_lex[2], temp_lex[3])
                            elif temp_lex[0] == "Constant":
                                n = Node(temp_lex[0], temp_lex[2])
                            elif temp_lex[0] == "Identifier":
                                n = Node(temp_lex[0], temp_lex[2])
                            else:
                                n = Node(temp_lex[0], temp_lex[1], temp_lex[2])

                            if i < len(lexs) - 1:
                                temp_lex2 = lexs[i + 1].split(";")

                            if temp_lex[0] == "Constant":
                                f.write(branch + f"{n.node_name} Node: \n{branch} -value: {n.value}\n")

                            elif temp_lex[0] == "DataType":
                                f.write(branch + f"{n.node_name} Node: \n{branch} -{n.type}\n")

                            elif temp_lex[0] == "Operation":
                                f.write(branch + f"{n.node_name} Node: \n{branch} -{n.type}\n")

                            elif temp_lex[0] == "Delimeter":
                                f.write(branch + f"{n.node_name} Node: \n{branch} -type: {n.type}\n")

                            else:
                                f.write(branch + f"{n.node_name} Node: \n{branch} -{n.type} \n{branch} -{n.v_name}\n")

                            if temp_lex[2] == "semicolon":
                                f.write(branch + "|\n" + branch + "----------------\n")
                                branch += "               "
                                f.write(branch + "|\n")





            else:
                print("ОШИБКА: Переданный файл пустой!")
                return False
        else:
            print("ОШИБКА: Переданный файл не существует!")
            return False
