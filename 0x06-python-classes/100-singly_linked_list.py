#!/usr/bin/python3
"""Singly linkde list module"""


class Node:
    """
    This is the Node class documentation.

    It defines a node of a singly linked list with private data
    and next_node attributes,
    getter/setter methods for data and next_node, and an instantiation method
    """

    def __init__(self, data, next_node=None):
        """
        Initializes a new instance of the Node class.

        Parameters:
        - data: The data value for the node.
        - next_node: The next node in the linked list. Defaults to None.

        Raises:
        -TypeError:If data is not an int or if next_node is not a Node object
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """
        Getter method to retrieve the data attribute.

        Returns:
        - int: The data value of the node.
        """
        return self.__data

    @data.setter
    def data(self, value):
        """
        Setter method to set the data attribute.

        Parameters:
        - value: The new data value for the node.

        Raises:
        - TypeError: If value is not an integer.
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """
        Getter method to retrieve the next_node attribute.

        Returns:
        - Node or None: The next node in the linked list.
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """
        Setter method to set the next_node attribute.

        Parameters:
        - value: The new next_node value for the node.

        Raises:
        - TypeError: If value is not a Node object or None.
        """
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """
    This is the SinglyLinkedList class documentation.

    It defines a singly linked list with a private head attribute,
    a simple instantiation method, a printable method, and a method to insert
    a new Node into the correct sorted position in the list (increasing order)
    """

    def __init__(self):
        """
        Initializes a new instance of the SinglyLinkedList class.

        The head attribute is set to None.
        """
        self.head = None

    def sorted_insert(self, value):
        """
        Inserts new Node into correct sorted posi in the list increasing order

        Parameters:
        - value: The data value for the new node.
        """
        new_node = Node(value)
        if not self.head or value < self.head.data:
            new_node.next_node = self.head
            self.head = new_node
            return

        current = self.head
        while current.next_node and current.next_node.data < value:
            current = current.next_node

        new_node.next_node = current.next_node
        current.next_node = new_node

    def __str__(self):
        """
        Returns a string representation of the linked list.

        Returns:
        - str: A string representation of the linked list.
        """
        result = []
        current = self.head
        while current:
            result.append(str(current.data))
            current = current.next_node
        return "\n".join(result)
