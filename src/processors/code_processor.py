import inspect
from src.nodes import class_node as c_node


class CodeProcessor:
    def __init__(self):
        self.modules = dict()

    def process_module(self, module):
        # Find any classes that exists within this module
        for (name, something) in inspect.getmembers(module):
            if inspect.isclass(something):
                self.process_class(something)

    def process_class(self, some_class):
        # Process the found class, and store in global modules
        # Find any functions with-in the class
        name = some_class.__name__
        module_name = some_class.__module__

        # create module for current file in global modules list
        if module_name not in self.modules:
            self.modules[module_name] = list()

        # create list of super classes for current class
        super_classes = self.fetch_super_classes(some_class)

        # create class object and append to current module
        class_node = c_node.ClassNode(name, super_classes)
        self.modules[module_name].append(class_node)

        # create list of functions & attributes in class
        self.fetch_attributes_and_functions(class_node, some_class)

    @staticmethod
    def fetch_super_classes(class_object):
        super_classes = list()

        for class_item in class_object.__bases__:
            if class_item.__name__ != 'object':
                if len(
                    list(
                        filter(
                            lambda x: x.__name__ != class_item.__name__,
                            super_classes))) == 0:
                    super_classes.append(class_item)

        return super_classes

    def fetch_attributes_and_functions(self, class_node, some_class):
        for (name, something) in inspect.getmembers(some_class):
            if inspect.ismethod(something) or inspect.isfunction(something):
                # get the class from the functions element
                function_class = something.__qualname__.split('.')[0]

                # only add function if the current class is the same as the
                # selected functions class
                if some_class.__name__ == function_class:
                    # create list of attributes in class with constructor
                    if something.__name__ == "__init__":
                        attributes = something.__code__.co_names

                        for attribute in attributes:
                            self.process_attribute(
                                attribute, class_node,
                                self.get_visibility_of_string(attribute))

                    self.process_function(
                        something,
                        class_node,
                        self.get_visibility_of_string(
                            something.__name__))

    @staticmethod
    def process_function(some_function, class_node, visibility):
        # Functions are added to the class node with just their title
        class_node.add_function(
            some_function.__name__,
            inspect.getfullargspec(some_function)[0],
            visibility)

    @staticmethod
    def process_attribute(attribute_name, class_node, visibility):
        filter_out_attributes = [
            "__doc__",
            "__module__",
            "__dict__",
            "__weakref__"]

        # Attributes are added to the class node with just their name
        if attribute_name not in filter_out_attributes:
            class_node.add_attribute(attribute_name, visibility)

    @staticmethod
    def get_visibility_of_string(string):
        """
        get visibility of function (public = +, protected = #, private = -)
        Author: Braeden
        >>> FileProcessor().get_visibility_of_string("test")
        '+'
        >>> FileProcessor().get_visibility_of_string("__test")
        '-'
        >>> FileProcessor().get_visibility_of_string("_test")
        '#'
        """
        visibility = "+"
        if string[:2] == "__":
            visibility = "-"
        elif string[0] == "_":
            visibility = "#"
        return visibility

    def get_modules(self):
        return self.modules
