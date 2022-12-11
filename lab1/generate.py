from Constants.constants import Constants


def generate(tree):
    tab = ""
    skip_tab = False
    with open("generated C code", 'w') as f:
        for i, node in enumerate(tree):
            #print(f"{i}: {node.node_name, node.value, node.type, node.v_name}")

            space = " "
            if i < len(tree) - 1:
                next_node = tree[i + 1]
                if next_node.type in ("semicolon", ")"):
                    space = ""

            match node.node_name:
                case "DataType":
                    if node.type == "boolean":
                        f.write("bool" + space)
                    else:
                        f.write(node.type + space)

                case "Variable":
                    if next_node.type in ("increment_operation", "decrement_operation"):
                        f.write(node.v_name)
                    elif node.type == "void" and node.v_name == "main":
                        f.write("int " + node.v_name)
                    else:
                        f.write(node.v_name + space)

                case "Operation":
                    for k, v in Constants.operators.items():
                        if v[1] == node.type:
                            f.write(k + space)

                case "Constant":
                    f.write(node.value + space)

                case "Delimeter":
                    if node.type == "semicolon":
                        if next_node.type == "}":
                            tab = tab.replace("\t", "", 1)
                            skip_tab = True
                        f.write(";\n" + tab)
                    elif node.type == "{":
                        tab += "\t"
                        f.write(node.type + "\n" + tab)
                    elif node.type == "}":
                        if next_node.type == "}":
                            tab = tab.replace("\t", "", 1)
                        f.write(node.type + "\n" + tab)
                    elif node.type == "(":
                        f.write(node.type)
                    else:
                        f.write(node.type + space)

                case "Identifier":
                    if node.value == "static" and next_node.value == "void" and tree[i+2].v_name == "main" or node.value == "void" and next_node.v_name == "main":
                        continue
                    if node.value in ("public", "String[]", "args"):
                        continue
                    f.write(node.value + space)

                case _:
                    pass

