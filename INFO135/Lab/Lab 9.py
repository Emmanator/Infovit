# Exercise 1
# a) Pre-order: H, A, D, E, C, B, G, F
# b) In-order: D, A, E, H, G, B, F, C
# c) Post-order: D, E, A, G, F, B, C, H

# Exercise 2
# Create a function build_my_tree() that creates the binary tree from exercise 1. Run
# Breadth First Search (BFS) starting from node ‘H’ and print all the visited nodes.
# You will need the BinaryTree from lecture 7 and the BFS algorithm from lecture 6.

class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None

    def insert_left(self, value):
        if self.left_child is None:
            self.left_child = BinaryTree(value)
        else:
            new_node = BinaryTree(value)
            new_node.left_child = self.left_child
            self.left_child = new_node

    def insert_right(self, value):
        if self.right_child is None:
            self.right_child = BinaryTree(value)
        else:
            new_node = BinaryTree(value)
            new_node.right_child = self.right_child
            self.right_child = new_node

    #    def breadth_first_search(self, node):
    #       searched = [node]
    #        search_queue = [node]
    #
    #        while search_queue:
    #            node = search_queue.pop(0)
    #
    #            print(f'[ {node}', end=' ]')
    #
    #            if node in self.graph:
    #                for neighbour in self.graph[node]:
    #                    if neighbour not in searched:
    #                        searched.append(neighbour)
    #                        search_queue.append(neighbour)

    def BFS(self, tree):
        queue = [tree]
        values = []

        while len(queue) != 0:
            current_node = queue.pop(0)
            values.append(current_node.value)

            if current_node.left_child is not None:
                queue.append(current_node.left_child)
            if current_node.right_child is not None:
                queue.append(current_node.right_child)

        return values


def build_my_tree():
    tree_node = BinaryTree('h')

    tree_node.insert_left('a')
    tree_node.insert_right('c')

    node_a = tree_node.left_child
    node_a.insert_left('d')
    node_a.insert_right('e')

    node_c = tree_node.right_child
    node_c.insert_right('b')

    node_b = node_c.right_child
    node_b.insert_right('g')
    node_b.insert_left('f')
    return tree_node


my_tree = build_my_tree()
print(my_tree.BFS(my_tree))


# Exercise 3
class BinarySearchTree:

    def __init__(self, value=None):
        self.value = value

        if self.value:
            self.left_child = BinarySearchTree()
            self.right_child = BinarySearchTree()

        else:
            self.left_child = None
            self.right_child = None

    def is_empty(self):
        return self.value is None

    def insert(self, value):
        if self.is_empty():
            self.value = value
            self.left_child = BinarySearchTree()
            self.right_child = BinarySearchTree()

        elif value < self.value:
            self.left_child.insert(value)

        elif value > self.value:
            self.right_child.insert(value)

    def in_order(self):
        if self.is_empty():
            return []
        else:
            return self.left_child.in_order() + [self.value] + self.right_child.in_order()

    def print_tree(self):
        print(self.in_order())

    def find(self, value):
        if self.is_empty():
            return False
        elif value == self.value:
            return True
        elif self.value > value:
            return self.left_child.find(value)
        elif self.value < value:
            return self.right_child.find(value)

    def is_leaf(self):
        return self.left_child.is_empty() and self.right_child.is_empty()

    def make_empty(self):
        self.value = None
        self.left_child = None
        self.right_child = None

    def copy_child(self, child):
        if child == 'left':
            self.value = self.left_child.value
            self.right_child = self.left_child.right_child
            self.left_child = self.left_child.left_child
        elif child == 'right':
            self.value = self.right_child.value
            self.left_child = self.right_child.left_child
            self.right_child = self.right_child.right_child

    def delete(self, value):
        if self.is_empty():
            print('empty tree')

        elif value < self.value:
            self.left_child.delete(value)

        elif value > self.value:
            self.right_child.delete(value)

        elif value == self.value:
            if self.is_leaf():
                self.make_empty()
            elif self.left_child.is_empty():
                self.copy_child('right')
            else:
                self.value = self.left_child.delete_max()

    def delete_max(self):
        if self.right_child.is_empty():
            max_val = self.value
            if self.left_child.is_empty():
                self.make_empty()
            else:
                self.copy_child('left')
            return max_val
        else:
            return self.right_child.delete_max()

    def pre_order(self):
        if self.is_empty():
            return []
        else:
            return [self.value] + self.left_child.pre_order() + self.right_child.pre_order()

    def post_order(self):
        if self.is_empty():
            return []
        else:
            return self.left_child.post_order() + self.right_child.post_order() + [self.value]


my_tree2 = BinarySearchTree()

my_tree2.insert('h')
my_tree2.insert('a')
my_tree2.insert('d')
my_tree2.insert('e')
my_tree2.insert('c')
my_tree2.insert('b')
my_tree2.insert('g')
my_tree2.insert('f')
my_tree2.find(max(my_tree2))

# Exercise 4
# O(1)
