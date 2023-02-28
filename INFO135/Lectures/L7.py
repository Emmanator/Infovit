# dijkstra algo

class Graph:
    graph = dict()

    def dijkstra(self):
        visited = []
        node = self.find_lowest_cost(visited)

        while node is not None:
            print(f' ')
            cost = self.costs[node]
            neighbors = self.graph[node]

            for n in neighbors.keys():
                new_cost = cost + neighbors[n]
                if self.costs[n] > new_cost:
                    self.costs[n] = new_cost

            visited.append(node)

    def find_lowest_cost(self, visited):
        lowest_cost = float('inf')
        lowest_cost_node = None

        for node in self.costs:
            cost = self.costs[node]
            if cost < lowest_cost and node not in visited:
                lowest_cost = cost
                lowest_cost_node = node

        return lowest_cost_node

    def set_costs(self, costs):
        self.costs = costs


# Binary Tree Class
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

    def inser_right(self, value):
        if self.right_child is None:
            self.right_child = BinaryTree(value)

        else:
            new_node = BinaryTree(value)
            new_node.right_child = self.right_child
            self.right_child = new_node


# Binary tree with lists
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


# Heap Sort implementation
def heapify(array, n, i):
    maximum = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and array[i] < array[left]:
        maximum = left

    if right < n and array[maximum] < array[right]:
        maximum = right

    if maximum != i:
        array[i], array[maximum] = array[maximum], array[i]

        heapify(array, n, maximum)


def heap_sort(arr):
    size = len(arr)

    for i in range(size, 0, -1):
        heapify(arr, size, i)

    for i in range(size - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)


my_array = [100, 84, 71, 60, 23, 12, 29, 1, 37, 4]

heap_sort(my_array)
print(my_array)
