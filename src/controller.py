from src.processors import file_processor
from src.processors import code_processor
from src import uml_output as uml_out


class Controller:
    def __init__(self, hide_attributes, hide_methods):
        self.hide_attributes = hide_attributes
        self.hide_methods = hide_methods
        self.filer = file_processor.FileProcessor()
        self.interpreter = code_processor.CodeProcessor()

    def parse_files(self, files):
        self.filer.process_files(files)

        for module in self.filer.get_modules():
            self.interpreter.process_module(module)

    def create_class_diagram(self):
        new_uml = uml_out.MakeUML(self.hide_attributes, self.hide_methods)
        new_uml.create_class_diagram(self.interpreter.get_modules())
