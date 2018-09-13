# Takes input form the command line and initiates the controller
# passing command line input to the controller which then uses
# the information to initiate the model which parses the require file/files
import argparse
import sys
import python_controller as pc


def initiate_python_parser():
    controller = pc.Controller()
    controller.run_console()


if __name__ == '__main__':
    initiate_python_parser()
    import doctest

    doctest.testmod()
