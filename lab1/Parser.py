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
        if not os.path.exists(path):
            print("ОШИБКА: Переданный файл не существует!")
            return False

        if os.stat(path).st_size == 0:
            print("ОШИБКА: Переданный файл пустой!")
            return False


        with open(path, "r") as f:
            Parser.main_str = f.read()
            lexs = Parser.main_str.split("\n")

        branch = ""
        do_flag = False
        void_flag = False
        error = ""
        last_v = ""
        err_str = 1

        with open("tree.txt", "w") as f:
            print(lexs)
            for i, l in enumerate(lexs):
                if l != "":
                    temp_lex = l.split(";")
                    if temp_lex[0] == "Variable":
                        n = Node(temp_lex[0], temp_lex[1], temp_lex[2], temp_lex[3])
                        last_v = temp_lex[2]

                    elif temp_lex[0] == "Constant":
                        if error == "":
                            if last_v == "int" and not temp_lex[2].isnumeric():
                                error = "Illegal type exception on line " + str(err_str)
                            elif last_v == "String" and temp_lex[2].isdigit():
                                error = "Illegal type exception on line " + str(err_str)
                            elif last_v == "boolean" and temp_lex[2] != "true" and temp_lex[2] != "false":
                                error = "Illegal type exception on line " + str(err_str)

                        n = Node(temp_lex[0], temp_lex[2])
                    elif temp_lex[0] == "Identifier":
                        n = Node(temp_lex[0], temp_lex[2])
                    else:
                        n = Node(temp_lex[0], temp_lex[1], temp_lex[2])

                    if i < len(lexs) - 1:
                        temp_lex2 = lexs[i + 1].split(";")

                    if temp_lex[0] == "Identifier" and temp_lex[2] == "do":
                        do_flag = True

                    if temp_lex[0] == "Variable" and temp_lex[2] == "class" and temp_lex2[0] == "Delimeter":
                        f.write(branch + f"{n.node_name} Node: \n{branch} -value: {n.v_name}\n")
                        f.write(branch + "|\n" + branch + "----------------\n")
                        branch += "               "
                        f.write(branch + "|\n")
                        continue

                    if temp_lex[0] == "Variable" and temp_lex[2] == "void":
                        void_flag = True

                    if temp_lex[0] == "Delimeter" and temp_lex[2] == "{":
                        err_str += 1

                    if temp_lex[0] == "Delimeter" and temp_lex[2] == "{" and void_flag:
                        void_flag = False
                        f.write(branch + f"{n.node_name} Node: \n{branch} -value: {n.type}\n")
                        f.write(branch + "|\n" + branch + "----------------\n")
                        branch += "               "
                        f.write(branch + "|\n")
                        continue

                    if temp_lex[0] == "Delimeter" and temp_lex2[0] == "Delimeter" and temp_lex[2] == "}" and temp_lex2[2] == "}":
                        f.write(branch + f"{n.node_name} Node: \n{branch} -type: {n.type}\n")
                        f.write(branch + "|\n" + branch + "----------------\n")
                        branch += "               "
                        f.write(branch + "|\n")
                        continue

                    if temp_lex[0] == "Constant":
                        f.write(branch + f"{n.node_name} Node: \n{branch} -value: {n.value}\n")

                    elif temp_lex[0] == "DataType":
                        f.write(branch + f"{n.node_name} Node: \n{branch} -{n.type}\n")

                    elif temp_lex[0] == "Operation":
                        f.write(branch + f"{n.node_name} Node: \n{branch} -{n.type}\n")

                    elif temp_lex[0] == "Delimeter":
                        f.write(branch + f"{n.node_name} Node: \n{branch} -type: {n.type}\n")

                    elif temp_lex[0] == "Identifier":
                        f.write(branch + f"{n.node_name} Node: \n{branch} -type: {n.value}\n")

                    else:
                        f.write(branch + f"{n.node_name} Node: \n{branch} -{n.type} \n{branch} -{n.v_name}\n")

                    if temp_lex[2] == "semicolon" and i != len(lexs) - 2:
                        err_str += 1
                        f.write(branch + "|\n" + branch + "----------------\n")
                        branch += "               "
                        f.write(branch + "|\n")
            if error != "":
                print("Error: " + error)

