import sys
import os


class FileProcessor:
    """
    Process multiple files ready to be interpreted by code processor
    Author: Braeden
    """

    def __init__(self):
        self.modules = list()

    def process_files(self, file_names):
        """
        Loop through a list of files, and process each file as an individual
        Author: Braeden
        >>> fp.process_files(["plants.py"])
        1
        >>> fp.process_files(["plants.py", "LinkedListNode.py"])
        2
        """
        for file in file_names:
            self.process_file(file)
        return len(self.modules)

    def process_file(self, file_name):
        # Import specified file_name and store as module
        path, file = os.path.split(file_name)
        module_name = file.replace(
            "./",
            "").replace(
            ".py",
            "").replace(
            "/",
            ".")

        # change path for import to directory of file
        sys.path.append(path)

        try:
            __import__(module_name, locals(), globals())
            self.modules.append(sys.modules[module_name])
        except ImportError:
            print("A file with this name could not be found, please try again.")
        except OSError:
            print("The provided python file contains invalid syntax, "
                  "please fix the provided code before running")
        except:
            print("Query Failed: An unexpected exception")

    def get_modules(self):
        return self.modules
