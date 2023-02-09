# lab 2

# Node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node1.next = node2
node2.next = node3


# Linked List
class Linkedlist:
    def __init__(self):
        self.head = None

    def add(self, new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

a = Linkedlist
a.add(a, 'test')
