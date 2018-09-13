from tkinter import filedialog, Tk

from src import model, uml_output as uml_out
from cmd import Cmd
from subprocess import call
import argparse


class Controller(Cmd):
    def __init__(self):
        Cmd.__init__(self)
        # Command line argument variables
        self.files = None
        self.statistics = None
        self.extracted_modules = None
        self.output = None
        self.args = self.register_arguments()
        self.parse_arguments()
        self.prompt = '> '

    # Created By Jake
    def run_console(self):
        self.cmdloop('Starting prompt...\n'
                     'Type "help" for commands')

    # Created by Jake
    def register_arguments(self):
        # Create your commands in here
        parser = argparse.ArgumentParser()
        # Created by Braeden
        parser.add_argument(
            "-f",
            "--file",
            nargs="+",
            help="Multiple file input for parse")
        # Created By Jake Reddock
        parser.add_argument(
            "-s",
            "--statistics",
            action='store_true',
            help="Print Statistics for classes uploaded")
        # Created By Michael Huang
        parser.add_argument(
            "-o",
            "--output",
            help="Setting name of the output location")
        return parser.parse_args()

    # Created By Jake Reddock
    def parse_arguments(self):
        # Create Logic for your arguments here
        # Created by Braeden
        if self.args.file is not None:
            self.files = self.args.file
            print("Files selected: ")
            print(*self.files, sep="\n")
        # Created by Michael Huang
        if self.args.output is not None:
            self.output = self.args.output
            print("Now setting names of output files")

    def do_change_python_files(self, args):
        """
        Change input files that are to be parsed by system
        Author: Braeden
        Syntax: change_python_files <filenames.py>
        """
        user_args = args.split()
        if len(user_args) > 0:
            self.files = [args]
        else:
            print("Syntax Error: change_python_files <filenames.py>")

    # Edited By Jake
    def do_output_to_dot(self, args):
        """
        Parse and output the file into a UML diagram
        Author: Braeden
        Syntax: output_to_dot [-a|-m]
        [-a] Hides all attributes on class diagram
        [-m] Hides all methods on class diagram
        """
        user_options = args.split()

        hide_attributes = False
        hide_methods = False

        if len(user_options) > 0:
            if "-a" in user_options:
                hide_attributes = True
            if "-m" in user_options:
                hide_methods = True

        self.run_parser(self, hide_attributes, hide_methods)

    def do_set_input_file(self, args):
        """
        Sets the input file that will be converted into a UML diagram.
        Author: Jake Reddock
        Syntax: set_input_file [file_name]
        """
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
        if self.files == "":
            print("No input file selected.")
        else:
            print("Input file selected:")
            print(*self.files, sep="\n")

    # Created by Michael Huang
    def do_output_to_file(self, args):
        """
        Sets the output of the class diagram to a file location.
        Author: Michael Huang
        Syntax: output_to_file
                output_to_file [path]
        """

        from shutil import copyfile
        if len(args) == 0:

            root = Tk()
            root.filename = filedialog.askdirectory()
            print(root.filename)
            root.withdraw()

            copyfile('tmp/class.png', root.filename + '/class.png')
        else:
            try:
                copyfile('tmp/class.png', args + '/class.png')
                print('The output to the file destination was successful.')
            except FileNotFoundError as f:
                print('Failed to find a file: %s' % f)
                print('Please specify a valid file path.')
            except:
                print('Unexpected error has occurred.')

    @staticmethod
    def do_output_to_png(args):
        """
        Converts dot file into PNG
        Author: Braeden
        """
        return call(['dot', '-Tpng', 'tmp/class.dot', '-o', 'tmp/class.png'])

    # Edited by Jake
    @staticmethod
    def run_parser(self, hide_attributes, hide_methods):
        if len(self.files) > 0:
            # Initiate processor
            processor = model.FileProcessor()
            processor.process_files(self.files)

            self.extracted_modules = processor.get_modules()

            new_uml = uml_out.MakeUML(hide_attributes, hide_methods)
            return new_uml.create_class_diagram(self.extracted_modules)
        else:
            print("Error: No files were set, use command change_python_files")

    def do_quit(self, other):
        '''
        Quits programme.
        Author: Peter
        '''
        print("Goodbye ......")
        return True
