from src.nodes import attribute_node as a_node, function_node as f_node


class ClassNode:
    """
    Class object containing attributes and functions
    Author: Braeden
    Contributor: Peter

    >>> ClassNode("Class One", []).name
    'Class One'
    >>> class_one = ClassNode("Class One")
    >>> class_one.add_attribute("Attribute One", "+")
    >>> class_one.add_attribute("Attribute Two", "+")
    >>> len(class_one.attributes)
    2
    """

    def __init__(self, name, super_classes=None):
        self.name = name
        self.attributes = []
        self.functions = []
        if super_classes is None:
            self.super_classes = list()
        else:
            self.super_classes = super_classes

    def add_attribute(self, attribute_name, visibility):
        self.attributes.append(a_node.AttributeNode(attribute_name, visibility))

    def add_function(self, function_name, list_of_parameters, visibility):
        self.functions.append(f_node.FunctionNode(function_name, list_of_parameters, visibility))

    def add_super_class(self, super_class):
        self.super_classes.append(super_class)
