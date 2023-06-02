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
            return

        last_node = self.head

        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def add_at_beginning(self, new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            return

        new_node.next = self.head
        self.head = new_node
        # print(self.head)

    def print_list(self):
        temp = self.head
        while temp:
            print(f'{temp.data} ', end='')
            temp = temp.next
        print("")

my_list = Linkedlist()
my_list.add_at_beginning(4)
my_list.add_at_beginning(3)
my_list.add_at_beginning(2)
my_list.add_at_beginning(1)
my_list.print_list()