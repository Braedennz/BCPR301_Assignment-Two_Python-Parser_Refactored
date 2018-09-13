class FunctionNode:
    """
    Function object containing function name and parameters
    Author: Braeden

    >>> FunctionNode("Function One", [], "+").get_name()
    'Function One'
    >>> len(FunctionNode("Function One",
    ... ["Param One", "Param Two"], "+").parameters)
    2
    """

    def __init__(self, name, list_of_parameters, visibility):
        self.name = name
        self.parameters = list_of_parameters
        self.visibility = visibility

    def get_name(self):
        return self.name

    def get_parameters(self):
        return ",".join(self.parameters)