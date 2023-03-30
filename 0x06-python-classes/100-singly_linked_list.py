#!/usr/bin/python3
'''
implement a singly-linked list data structure in python
'''


class Node:
    '''
    Define a node of a singly-linked list

    Attributes:
    data(int): the content of a node
    next_node(list): the next node (or a pointer to it)
    '''
    def __init__(self, data, next_node=None):
        '''
        initialize a node with data and pointer to next node

        Args:
        data(int): the data for the node
        next_node(list, optional): pointer to the next node, i.e the
        name of next node
        '''
        if type(data) == int:
            self.__data = data
        else:
            raise TypeError('data must be an integer')

        if next_node is None or type(next_node) == type(Node):
            self.__next_node = next_node
        else:
            raise TypeError('next_node must be a Node object')

    @property
    def data(self):
        '''
        set and retrieve the content of a node

        Args:
        value(int, for setter alone): the data to assign to node

        Returns:
        int(for getter alone): the node's data to be returned

        Raises:
        TypeError(for setter alone): when data to insert to node isn't int
        '''
        return self.__data

    @data.setter
    def data(self, value):
        if type(value) == int:
            self.__data = value
        else:
            raise TypeError('data must be an integer')

    @property
    def next_node(self):
        '''
        set and retrieve the next node pointer/element of a node

        Args:
        value(list, for setter alone): the next node or its
        name(a pointer to it)

        Returns:
        list(for getter alone): the node to be returned

        Raises:
        TypeError(for setter alone): when the next node isn't a node
        object, or None
        '''
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if type(value) is not None or type(value) != type(Node):
            raise TypeError('next_node must be a Node object')
        else:
            self.__next_node = value


class SinglyLinkedList:
    '''
    define a singly-linked list

    Attributes;
    head(list or None): the head of the list
    '''
    def __init__(self):
        '''
        initialize the list
        '''
        self.__head = None

    def sorted_insert(self, value):
        '''
        insert a new node into a sorted position (in increasing order)
        in the list.

        Args:
        value(list): the node to insert
        '''
        new_node = Node(value, None)
        if self.__head is None:
            self.__head = new_node
        else:
            hold = self.__head
            while True:
                condition = hold.data <= new_node.data
                if hold.data >= new_node.data:
                    self.__head = new_node
                    new_node.next_node = hold
                    break
                elif hold.data <= new_node.data and hold.next_node is None:
                    hold.next_node = new_node
                    break
                elif condition and new_node.data <= hold.next_node.data:
                    new_node.next_node = hold.next_node
                    hold.next_node = new_node
                    break
                else:
                    hold = hold.next_node

    def __str__(self):
        hold = self.__head
        result = ''
        while hold is not None:
            result += str(hold.data)
            if hold.next_node is not None:
                result += '\n'
            hold = hold.next_node
        return result

n1 = Node(3)
print(n1.data)

n2 = Node(-5)
print(n2.data)

n3 = Node(4)
n3.nextnode = n2
print(n3.nextnode.data)

try:
    n4 = Node("5")
except Exception as e:
    print(e)

try:
    n2.next_node = "Node"
except Exception as e:
    print(e)
