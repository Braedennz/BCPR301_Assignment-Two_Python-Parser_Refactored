import unittest
import model
import python_controller

class ModelTestCase(unittest.TestCase):
    """
    Tests for 'model.py'
    """

    individual_file_upload = ["plants.py"]

    def test_individual_file_processed(self):
        """
        Is individual module created after processing of file?
        Author: Braeden
        """
        file_processor = model.FileProcessor()
        modules = file_processor.process_files(self.individual_file_upload)

        self.assertTrue(modules == 1)

    def test_multiple_file_processed(self):
        """
        Is multiple modules created after processing of file?
        Author: Braeden
        """
        file_processor = model.FileProcessor()
        modules = file_processor.process_files(
            ["plants.py", "LinkedListNode.py"])

        self.assertTrue(modules == 2)

    def test_class_name(self):
        """
        Checks plants.py class names have been appended correctly
        Author: Braeden
        """
        file_processor = model.FileProcessor()
        file_processor.process_files(self.individual_file_upload)

        self.assertTrue(file_processor.modules['plants'][0].name is 'Orchid')

    def test_output_to_png(self):
        """
        Checks if creation of UML diagram and output to PNG file works
        Author: Braeden
        """
        ctrl = python_controller.Controller
        self.assertTrue(ctrl.do_output_to_png(None) is 0)

    def test_file_change(self):
        """
        Checks if file names that are stored from system
        arguments can be changed by function
        Author: Braeden
        """
        ctrl = python_controller.Controller
        ctrl.do_change_python_files(ctrl, "file_one.py file_two.py")

        self.assertTrue(ctrl.files[0] == "file_one.py")

    def test_public_function_symbol_checker(self):
        """
        Checks if the provided method name is
        private, public or protected
        Author: Braeden
        """
        md = model.FileProcessor()
        visibility = md.get_visibility_of_string("public_function")

        self.assertTrue(visibility == "+")

    def test_private_function_symbol_checker(self):
        """
        Checks if the provided method name is
        private, public or protected
        Author: Braeden
        """
        md = model.FileProcessor()
        visibility = md.get_visibility_of_string("__public_function")

        self.assertTrue(visibility == "-")

    def test_protected_function_symbol_checker(self):
        """
        Checks if the provided method name is
        private, public or protected
        Author: Braeden
        """
        md = model.FileProcessor()
        visibility = md.get_visibility_of_string("_public_function")

        self.assertTrue(visibility == "#")

    def test_create_class_with_name(self):
        """
        Checks if class name is equal to one created
        Author: Braeden
        """
        md = model.ClassNode("Class One", [])

        self.assertTrue(md.name == "Class One")

    def test_create_class_with_attributes(self):
        """
        Checks if class with attributes
        tests if correct as created are stored
        Author: Braeden
        """
        md = model.ClassNode("Class One", [])
        md.add_attribute("Attribute One", "+")
        md.add_attribute("Attribute Two", "+")

        self.assertTrue(len(md.attributes) == 2)

    def test_create_class_with_methods(self):
        """
        Checks if class with methods
        tests if correct as created are stored
        Author: Braeden
        """
        md = model.ClassNode("Class One", [])
        md.add_function("Function One", [], "+")
        md.add_function("Function Two", [], "+")

        self.assertTrue(len(md.functions) == 2)

    def test_create_class_with_super_classes(self):
        """
        Checks if class with methods
        tests if correct as created are stored
        Author: Braeden
        """
        md = model.ClassNode("Class One", [])
        md.add_super_class(())
        md.add_super_class(())

        self.assertTrue(len(md.super_classes) == 2)

    def test_create_function_with_name(self):
        """
        Checks if function name is equal to one created
        Author: Braeden
        """
        md = model.FunctionNode("Function One", [], "+")

        self.assertTrue(md.name == "Function One")

    def test_create_attribute_with_name(self):
        """
        Checks if attribute name is equal to one created
        Author: Braeden
        """
        md = model.AttributeNode("Attribute One", "+")

        self.assertTrue(md.name == "Attribute One")


if __name__ == '__main__':
    unittest.main()
