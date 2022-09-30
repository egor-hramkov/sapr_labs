from LexemProcessor import LexemProcessor
from Models.Lexem import Lexem
from Models.Variable import Variable


processor = LexemProcessor()
result = processor.process_file("example.txt")

print("Lexems:")

for l in LexemProcessor.list_lexems:
    print(Lexem.ToString(l))

print("===================================================================\nVariables:")
for v in LexemProcessor.list_variables:
    print(Variable.ToString(v))

print("===================================================================")