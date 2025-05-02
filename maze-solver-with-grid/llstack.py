"""
Kahlan Walcott
Date: 4/15/2024
This code is for project 3 in CIS 163. It recursively goes through a maze and puts the coordinates into a singly linked
list that is returned to the user.
"""

from node import Node


class LLStack:
    """
    This class crates and returns a singly linked list of a correct path through a maze.
    """
    def __init__(self):
        """
        This function sets up the head and the size of the stack.
        """
        self.__head = None
        self.__size = 0

    @property
    def size(self):
        """This function allows for size to be read only."""
        return self.__size

    def pop(self) -> tuple:
        """
        This function removes the top node on the stack and returns the data as a tuple stored at that node.
        """
        if self.__size == 0:  # when there is nothing in the stack you can't remove anything
            raise IndexError()

        removed = self.__head.data
        self.__head = self.__head.next
        self.__size -= 1
        return removed

    def push(self, data: tuple):
        """Ths function takes in data as a tuple and adds it to the top of the stack."""
        if not isinstance(data, tuple):  # when the data is not a tuple
            raise TypeError()

        for place in data:  # from Ashly (checks everything in the tuple)
            if not isinstance(place, int):  # if the information in the tuple is not an integer
                raise TypeError()
        else:  # the data is a tuple, and it contains integers, so it can be added to the stack
            added = Node(data)
            added.next = self.__head
            self.__head = added
            self.__size += 1

        if self.__size == 0:  # when the stack is empty add the data to the stack and increase the size by 1.
            self.__size += 1
            self.__head = Node(data)

    def __str__(self) -> str:  # from professor
        """This function returns the data in the stack as a string either with an arrow pointing to the next tuple or
        it is the end so no arrow is returned."""
        if self.__head:  # when there is something in the stack
            st = ''
            curr = self.__head
            while curr.next:  # run through the stack until you reach the end.
                st += curr.__str__() + ' -> '
                curr = curr.next
            st += curr.__str__()
            return st


