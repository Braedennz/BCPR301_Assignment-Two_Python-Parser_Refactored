# Takes input form the command line and initiates the controller
# passing command line input to the controller which then uses
# the information to initiate the model which parses the require file/files
from src import interpreter as pi


def initiate_python_parser():
    interpreter = pi.Interpreter()
    interpreter.run_console()


if __name__ == '__main__':
    initiate_python_parser()
    import doctest

    doctest.testmod()
