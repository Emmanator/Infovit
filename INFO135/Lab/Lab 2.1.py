# Lab 2

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, new_data):
        temp = Node(new_data)
        if self.head is None:
            self.head = temp
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = temp

    def add_at_beginning(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node


ll = LinkedList()
ll.add(1)
ll.add(2)
ll.add(3)
ll.add_at_beginning(0)
ll.add_at_beginning(123)
ll.add(123)

node = ll.head
print(node.data)

while node.next:
    node = node.next
    print(node.data)
