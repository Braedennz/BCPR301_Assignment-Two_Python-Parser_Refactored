import unittest
from src import controller
from src import interpreter
import os
import inspect
from src.processors import code_processor, file_processor
from src.nodes import attribute_node, class_node, function_node


class RefactoredTestCase(unittest.TestCase):
    """
    Tests for bad smell #1 : Large Class
    These tests check whether the commands are
    changing the controller when called with different arguments for each
    via the controller and interpreter
    """

    array_individual_file_upload = ['plants.py']
    array_multiple_file_upload = ['plants.py', 'plants2.py']

    string_individual_file_upload = 'plants.py'
    string_multiple_file_upload = 'plants.py  plants2.py'

    def test_controller_setting_uploaded_files(self):
        """
        Issue One - Large Class - Test One
        Tests is can call command to set files
        Author: Braeden
        """
        ctrl = controller.Controller()

        files_set = ctrl.set_files_by_arguments(
            self.array_multiple_file_upload)

        self.assertTrue(files_set and
                        ctrl.files == self.array_multiple_file_upload)

    def test_interpret_setting_uploaded_files(self):
        """
        Issue One - Large Class - Test Two
        Tests if can call interpreter to set files
        Author: Braeden
        """
        inter = interpreter.Interpreter()
        inter.do_change_python_files(self.string_multiple_file_upload)

        self.assertTrue(inter.controller.files ==
                        self.array_multiple_file_upload)

    def test_interpret_output_to_dot(self):
        """
        Issue One - Large Class - Test Three
        Tests if can call interpreter to create DOT file
        Author: Braeden
        """
        inter = interpreter.Interpreter()
        inter.controller.set_files_by_arguments(
            [os.getcwd() + "\\tmp\\plants.py"])
        inter.do_output_to_dot("")

        file_exists = os.path.isfile(os.getcwd() + "\\src\\tmp\\class.dot")

        self.assertTrue(file_exists)

    def test_controller_setting_output_files(self):
        """
        Issue One - Large Class - Test Four
        Tests if can call controller to change
            output to different directory
        Author: Braeden
        """
        ctrl = controller.Controller()
        output = ctrl.set_output_name_by_arguments(os.getcwd())

        self.assertTrue(output)

    """
    Tests for bad smell #2 : Long Method
    These tests check whether the functionality to create
    the dot file and class diagram is still working correctly,
    the tests are ran using the run_parser and code_processor
    """

    def test_run_parser_single(self):
        """
        Issue Two - Long Method - Test One
        Tests if can run parser using new re-structured method
        Uses run_parser to call new structure in code_processor class
        using single file
        Author: Braeden
        """
        ctrl = controller.Controller()
        ctrl.set_files_by_arguments([os.getcwd() + "\\tmp\\plants.py"])

        parsed = ctrl.run_parser(False, False)

        self.assertTrue(parsed)

    def test_run_parser_multiple(self):
        """
        Issue Two - Long Method - Test Two
        Tests if can run parser using new re-structured method
        Uses run_parser to call new structure in code_processor class
        using multiple files
        Author: Braeden
        """
        ctrl = controller.Controller()
        ctrl.set_files_by_arguments(
            [os.getcwd() + "\\tmp\\plants.py",
             os.getcwd() + "\\src\\controller.py"])

        parsed = ctrl.run_parser(False, False)

        self.assertTrue(parsed)

    def test_parser_super_classes(self):
        """
        Issue Two - Long Method - Test Three
        Tests if can get the amount of super classes Orchid
        class with-in plants.py belongs to
        Author: Braeden
        """
        fp = file_processor.FileProcessor()
        cp = code_processor.CodeProcessor()
        fp.process_file(os.getcwd() + "\\tmp\\plants.py")

        class_object = inspect.getmembers(fp.get_modules()[0])[0][1]
        super_classes = cp.fetch_super_classes(class_object)

        self.assertTrue(len(super_classes) == 1)

    """
    Tests for bad smell #3 : -

    """

    def test_create_function_node(self):
        """
        Issue Three - Alternative classes with different interfaces - Test One
        a
        Author: Braeden
        """
        f = function_node.FunctionNode("Function One",
                                       ["param one", "param two"], "+")

        self.assertTrue(f.get_name() == "Function One")

    def test_create_attribute_node(self):
        """
        Issue Three - Alternative classes with different interfaces - Test Two
        a
        Author: Braeden
        """
        a = attribute_node.AttributeNode("Attribute One", "+")

        self.assertTrue(a.get_name() == "Attribute One")

    def test_create_class_node(self):
        """
        Issue Three - Alternative classes with
        different interfaces - Test Three
        a
        Author: Braeden
        """
        c = class_node.ClassNode("Class One", None)

        self.assertTrue(c.get_name() == "Class One")


if __name__ == '__main__':
    unittest.main()
