class Variable:

    id = ""
    dataType = ""
    name = ""

    def __init__(self, _id, _dataType, _name):
        self.id = _id
        self.dataType = _dataType
        self.name = _name

    def __str__(self):
        return f"<{self.id}> Variable of type <{self.dataType}> with name <{self.name}>"


