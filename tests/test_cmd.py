import unittest
from src import controller
from src import interpreter
import os


class ModelTestCase(unittest.TestCase):
    """
    Tests for 'model.py'
    """

    array_individual_file_upload = ['../tmp/plants.py']
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

        files_set = ctrl.set_files_by_arguments(self.array_multiple_file_upload)

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

        self.assertTrue(inter.controller.files == self.array_multiple_file_upload)

    def test_interpret_output_to_dot(self):
        """
        Issue One - Large Class - Test Three
        Tests if can call interpreter to create DOT file
        Author: Braeden
        """
        inter = interpreter.Interpreter()
        inter.controller.set_files_by_arguments([os.getcwd() + "\\tmp\\plants.py"])
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


if __name__ == '__main__':
    unittest.main()
