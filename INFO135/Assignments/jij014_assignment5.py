# Assignment 5
# Exercise 1:
# They're all full binary trees

# Exercise 2:
def binary_tree(r):
    return [r, [], []]


def get_left_child(root):
    return root[1]


def get_right_child(root):
    return root[2]


def insert_left_child(root, new_branch):
    t = root.pop(1)
    if len(t) > 1:
        root.insert(1, [new_branch, t, []])
    else:
        root.insert(1, [new_branch, [], []])
    return root


def insert_right_child(root, new_branch):
    t = root.pop(2)
    if len(t) > 1:
        root.insert(2, [new_branch, [], t])
    else:
        root.insert(2, [new_branch, [], []])
    return root


def make_tree():
    my_tree = binary_tree(1)

    insert_left_child(my_tree, 2)
    insert_right_child(my_tree, 3)

    insert_left_child(get_left_child(my_tree), 4)

    insert_left_child(get_right_child(my_tree), 5)
    insert_right_child(get_right_child(my_tree), 6)
    return my_tree


print(make_tree())


# Exercise 3
class Graph:
    graph = dict()

    def add_edge(self, node, neighbour):
        if node not in self.graph:
            self.graph[node] = [neighbour]
        else:
            self.graph[node].append(neighbour)

    def print_graph(self):
        print(self.graph)

    def print_edges(self):
        for node in self.graph:
            for neighbour in self.graph[node]:
                print(f'({node}, {neighbour})')

    searched = []

    def depth_first_search(self, node):
        if node not in self.searched:

            print(f'[ {node} ', end=']')

            self.searched.append(node)
            if node in self.graph:
                for neighbour in self.graph[node]:
                    self.depth_first_search(neighbour)


def build_my_graph2():
    my_graph = Graph()

    my_graph.add_edge('a', 'b')
    my_graph.add_edge('a', 'c')
    my_graph.add_edge('b', 'c')
    my_graph.add_edge('b', 'd')
    my_graph.add_edge('c', 'e')
    my_graph.add_edge('d', 'g')
    my_graph.add_edge('d', 'h')
    my_graph.add_edge('d', 'e')
    my_graph.add_edge('e', 'f')
    my_graph.add_edge('f', 'c')

    print('DFS')
    my_graph.depth_first_search('a')
    print()


build_my_graph2()


# Exercise 4
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

    def compute_sum(self):
        if self.is_empty():
            return 0
        return self.left_child.compute_sum() + self.value + self.right_child.compute_sum()

    def compute_count(self):
        if self.is_empty():
            return 0
        return self.left_child.compute_count() + 1 + self.right_child.compute_count()


my_tree = BinarySearchTree()
my_tree.insert(2)
my_tree.insert(4)
my_tree.insert(6)
my_tree.insert(8)
my_tree.insert(10)

print('sum:', my_tree.compute_sum())
print('number of nodes:', my_tree.compute_count())
