class AttributeNode:
    """
    Attribute object containing attribute name
    Author: Braeden

    >>> AttributeNode("Attribute One", "+").name
    'Attribute One'
    """

    def __init__(self, name, visibility):
        self.name = name
        self.visibility = visibility
