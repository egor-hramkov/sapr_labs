from LexemProcessor import LexemProcessor
from Parser import Parser
from Models.Lexem import Lexem
from Models.Variable import Variable


processor = LexemProcessor()
result = processor.process_file("example.txt")

# print("Lexems:")
#
# for l in LexemProcessor.list_lexems:
#     print(l)
#
# print("===================================================================\nVariables:")
#
# for v in LexemProcessor.list_variables:
#     print(v)
#
# print("===================================================================")

with open("temp.txt", "w") as f:
    for elem in LexemProcessor.list_l_and_v:
        #print(elem)
        if isinstance(elem, Lexem):
            f.write(f"{elem.type};{elem.id};{elem.value}\n")
        if isinstance(elem, Variable):
            f.write(f"Variable;{elem.id};{elem.dataType};{elem.name}\n")

pars = Parser.make_tree("temp.txt")
