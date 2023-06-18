#!/usr/bin/python3
"""Sigly linked list"""


class Node:
    """Singly linked list Node definition"""

    def __init__(self, data, next_node=None):
        """Node initializer"""
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Getter method"""
        return self.__data

    @data.setter
    def data(self, value):
        """Setter method"""
        if type(value) != int:
            raise ValueError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Getter method"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Setter method"""
        if value is not None and type(value) != Node:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Singly linked list defition"""

    def __init__(self):
        """Singly linked list initialization"""
        self.__head = None

    def sorted_insert(self, value):
        """Iserts a new Node into the correct sorted position"""

        newn = Node(value)
        newn.data = value
        idxr = self.__head
        iab = 0

        if not self.__head:
            self.__head = newn
        else:
            if value < idxr.data:
                iab = 1
                newn.next_node = idxr
                self.__head = newn

            while idxr.next_node and value > idxr.next_node.data and not iab:
                idxr = idxr.next_node

            if not iab:
                newn.next_node = idxr.next_node
                idxr.next_node = newn

    def __str__(self):
        """Defines the output of the SLL"""

        idxr = self.__head
        sllstr = ""

        while idxr:
            sllstr += str(idxr.data) + "\n"
            idxr = idxr.next_node

        return sllstr[:-1]
