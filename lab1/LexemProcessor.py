from Constants.LexemTypes import LexemTypes
from Models.Lexem import Lexem
from Models.Variable import Variable
from Constants.constants import Constants


class LexemProcessor:
    main_string = ""
    list_lexems = []
    list_variables = []
    list_name_variables = []
    variable_cnt = 0
    last_variable = ""
    buffer = ""
    flag_inc = False

    @staticmethod
    def process_file(path: str):
        with open(path, 'r', encoding='utf-8') as file:
            main_string = file.read()
            #main_lst = [s for s in main_string if s != '\n' and s != ' ']
            main_lst = list(main_string)
            for i, obj in enumerate(main_lst):
                if LexemProcessor.flag_inc:
                    # LexemProcessor.buffer = ""
                    LexemProcessor.flag_inc = False
                    continue

                if obj == '\n' or obj == ' ' or obj == ';' or obj == '{' or obj == '}' or obj == '(' or obj == ')' or obj == '+' or obj == '-' or obj == '*' or obj == '/':
                    if LexemProcessor.buffer in Constants.types:
                        LexemProcessor.add_lexem(LexemProcessor.buffer)

                    elif obj == '+' and main_lst[i+1] == '+' or obj == '-' and main_lst[i+1] == '-':
                        LexemProcessor.add_lexem(LexemProcessor.buffer)
                        LexemProcessor.buffer = "" + obj + main_lst[i + 1]
                        LexemProcessor.flag_inc = True
                        continue

                    elif obj == '*' and main_lst[i+1] == '=' or obj == '/' and main_lst[i+1] == '=' or obj == '%' and main_lst[i+1] == '=' or obj == '+' and main_lst[i+1] == '=' or obj == '-' and main_lst[i+1] == '=' :
                        LexemProcessor.add_lexem(LexemProcessor.buffer)
                        LexemProcessor.buffer = "" + obj + main_lst[i + 1]
                        LexemProcessor.flag_inc = True
                        continue

                    elif LexemProcessor.buffer in Constants.operators:
                        LexemProcessor.add_lexem(LexemProcessor.buffer)

                    elif LexemProcessor.buffer in Constants.Keywords:
                        LexemProcessor.add_lexem(LexemProcessor.buffer)

                    elif LexemProcessor.buffer in Constants.KeySymbols:
                        LexemProcessor.add_lexem(LexemProcessor.buffer)

                    elif LexemProcessor.buffer.isdigit():
                        LexemProcessor.add_lexem(LexemProcessor.buffer)

                    else:
                        LexemProcessor.add_variable(LexemProcessor.buffer)

                    if obj == '\n' or obj == ' ':
                        LexemProcessor.buffer = ""
                    elif obj == '(' or obj == '{':
                        LexemProcessor.buffer = obj
                        LexemProcessor.add_lexem(LexemProcessor.buffer)
                        LexemProcessor.buffer = ""
                    else:
                        LexemProcessor.buffer = obj
                else:
                    LexemProcessor.buffer += obj
            LexemProcessor.add_lexem(LexemProcessor.buffer)
            print("list = ", main_lst)

        return main_string

    @staticmethod
    def add_lexem(strlex: str):
        if strlex in Constants.types:
            l = Lexem("DataType", Constants.types[strlex][0], Constants.types[strlex][1])
            LexemProcessor.list_lexems.append(l)
            LexemProcessor.last_variable = strlex
        elif strlex in Constants.operators:
            l = Lexem("Operation", Constants.operators[strlex][0], Constants.operators[strlex][1])
            LexemProcessor.list_lexems.append(l)
        elif strlex in Constants.Keywords:
            l = Lexem("Identifier", Constants.Keywords[strlex][0], Constants.Keywords[strlex][1])
            LexemProcessor.list_lexems.append(l)
            LexemProcessor.last_variable = strlex
        elif strlex in Constants.KeySymbols:
            l = Lexem("Delimeter", Constants.KeySymbols[strlex][0], Constants.KeySymbols[strlex][1])
            LexemProcessor.list_lexems.append(l)
        elif strlex.isdigit():
            l = Lexem("Constant", 0, strlex)
            LexemProcessor.list_lexems.append(l)

    @staticmethod
    def add_variable(name: str):
        if name != "" and name not in LexemProcessor.list_name_variables:
            LexemProcessor.list_name_variables.append(name)
            v = Variable(LexemProcessor.variable_cnt, LexemProcessor.last_variable, name)
            LexemProcessor.list_variables.append(v)
            LexemProcessor.variable_cnt += 1