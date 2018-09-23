from src.processors import file_processor
from src.processors import code_processor
from src import uml_output as uml_out

from tkinter import filedialog, Tk
from shutil import copyfile
from subprocess import call
import os


class Controller:
    def __init__(self):
        self.filer = file_processor.FileProcessor()
        self.parser = code_processor.CodeProcessor()
        self.files = None
        self.output = None

    def set_files_by_arguments(self, files):
        if files is not None:
            self.files = files
            return True

        return False

    def set_output_name_by_arguments(self, output):
        if output is not None:
            self.output = output
            return True

        return False

    def cl_set_python_files(self, args):
        user_args = args.split()

        if len(user_args) > 0:
            self.files = user_args
            return True

        return False

    def ui_set_python_files(self, args):
        if len(args) == 0:
            root = Tk()
            self.files = filedialog.askopenfilenames(
                initialdir="C:/",
                title="Select Input File",
                filetypes=(
                    ("Python Files",
                     "*.py"),
                    ("all files",
                     "*.*")))
            root.withdraw()
        else:
            self.files = [args]

        if self.files != "":
            return True

        return False

    def copy_file_to_destination(self, args):
        if len(args) == 0:
            root = Tk()
            root.filename = filedialog.askdirectory()
            root.withdraw()
            copyfile('tmp/class.png', root.filename + '/class.png')
            return True
        try:
            copyfile('tmp/class.png', args + '/class.png')
            return True
        except FileNotFoundError as f:
            print('Failed to find a file: %s' % f)
            print('Please specify a valid file path.')
            return False
        except BaseException:
            print('Unexpected error has occurred.')
            return False

    @staticmethod
    def convert_dot_to_png():
        os.chdir(os.getcwd() + '/src')
        return call(['dot', '-Tpng', 'tmp/class.dot', '-o', 'tmp/class.png'])

    def run_parser(self, hide_attributes, hide_methods):
        if len(self.files) == 0:
            return False

        if self.filer.process_files(self.files) == 0:
            return False

        for module in self.filer.get_modules():
            self.parser.process_module(module)

        new_uml = uml_out.MakeUML(hide_attributes, hide_methods)
        return new_uml.create_class_diagram(self.parser.get_modules())
