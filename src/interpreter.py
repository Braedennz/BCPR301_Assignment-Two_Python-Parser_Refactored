from src import controller
from cmd import Cmd
import argparse


def handle_message(message_type, message):
    print("{0}: {1}".format(message_type, message))


def register_arguments():
    # Create your commands in here
    parser = argparse.ArgumentParser()
    # Created by Braeden
    parser.add_argument(
        "-f",
        "--file",
        nargs="+",
        help="Multiple file input for parse")
    # Created By Michael Huang
    parser.add_argument(
        "-o",
        "--output",
        help="Setting name of the output location")
    return parser.parse_args()


class Interpreter(Cmd):
    def __init__(self):
        Cmd.__init__(self)
        # Command line argument variables
        self.statistics = None
        self.extracted_modules = None
        self.args = register_arguments()
        self.prompt = '> '
        self.controller = controller.Controller()
        self.parse_arguments()

    def run_console(self):
        self.cmdloop('Starting prompt...\n'
                     'Type "help" for commands')

    def parse_arguments(self):
        if self.controller.set_files_by_arguments(self.args.file):
            handle_message("Success", "files were set by arguments")

        if self.controller.set_output_name_by_arguments(self.args.output):
            handle_message("Success", "file output name is set by arguments")

    def do_change_python_files(self, args):
        """
        Change input files that are to be parsed by system
        Author: Braeden
        Syntax: change_python_files <filenames.py>
        """
        if self.controller.cl_set_python_files(args):
            handle_message("Success", "files have been set")
        else:
            handle_message("Error", "change_python_files <filenames.py>")

    def do_set_input_file(self, args):
        """
        Sets the input file that will be converted into a UML diagram.
        Author: Jake Reddock
        Syntax: set_input_file [file_name]
        """
        if self.controller.ui_set_python_files(args):
            handle_message("Success", "files have been set")

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

        if self.controller.run_parser(hide_attributes, hide_methods):
            handle_message("Success", "dot file has been created")
        else:
            handle_message("Error", "error handling files, please check input")

    def do_output_to_file(self, args):
        """
        Sets the output of the class diagram to a file location.
        Author: Michael Huang
        Syntax: output_to_file
                output_to_file [path]
        """

        if self.controller.copy_file_to_destination(args):
            handle_message("Success", "copied file to the destination")

    def do_output_to_png(self, args):
        """
        Converts dot file into PNG
        Author: Braeden
        """

        if not self.controller.convert_dot_to_png():
            handle_message(
                "Success",
                "created png file in specified destination")
        else:
            handle_message(
                "Error", "failed to create png file in specified destination")
