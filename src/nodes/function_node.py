from src.nodes import node as i_node


class FunctionNode(i_node.Node):
    def __init__(self, name, list_of_parameters, visibility):
        i_node.Node.__init__(self, name)
        self.parameters = list_of_parameters
        self.visibility = visibility

    def get_parameters(self):
        return ",".join(self.parameters)
