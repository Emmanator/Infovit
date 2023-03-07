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


my_tree = BinarySearchTree()
my_tree.insert(3)
my_tree.insert(1)
my_tree.insert(4)
my_tree.insert(2)
my_tree.insert(5)

my_tree.print_tree()

print(my_tree.find(4))
