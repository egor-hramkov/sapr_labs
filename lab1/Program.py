from LexemProcessor import LexemProcessor
from Parser import Parser
from Models.Lexem import Lexem
from Models.Variable import Variable
from generate import generate


result = LexemProcessor.process_file("example3.txt")

print("Lexems:")

for l in LexemProcessor.list_lexems:
    print(l)

print("===================================================================\nVariables:")

for v in LexemProcessor.list_variables:
    print(v)

print("===================================================================")

with open("temp.txt", "w") as f:
    for elem in LexemProcessor.list_l_and_v:
        #print(elem)
        if isinstance(elem, Lexem):
            f.write(f"{elem.type};{elem.id};{elem.value}\n")
        if isinstance(elem, Variable):
            f.write(f"Variable;{elem.id};{elem.dataType};{elem.name}\n")

pars = Parser.make_tree("temp.txt")

# for t in Parser.tree:
#     print(t.node_name, t.value, t.type, t.v_name)
#generate_code("temp.txt")
generate(Parser.tree)
