from src.nodes import node as i_node


class AttributeNode(i_node.Node):
    def __init__(self, name, visibility):
        i_node.Node.__init__(self, name)
        self.visibility = visibility
