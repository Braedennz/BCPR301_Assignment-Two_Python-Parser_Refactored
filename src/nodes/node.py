from abc import ABCMeta, abstractmethod


class Node(metaclass=ABCMeta):

    def __init__(self, name):
        self.name = name



    def get_name(self):
        return self.name