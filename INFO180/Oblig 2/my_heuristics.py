from heuristic import Heuristic
from grid_walk_node import GridWalkNode
from make_grid import SIZE
import math


# 3)
class ZeroH(Heuristic):

    def __init__(self):
        self.target = GridWalkNode(0, 0)

    def h(self, node):
        return max(abs(node.i - self.target.i), abs(node.j - self.target.j))


# 4)
class EuclidH(Heuristic):

    def __init__(self):
        self.target = GridWalkNode(0, 0)

    def h(self, node):
        return math.sqrt(((SIZE - node.i) ** 2) + (SIZE - node.j) ** 2)


# 5)
class Task3_2(Heuristic):

    def __init__(self):
        self.target = GridWalkNode(0, 0)

    def h(self, node):
        return max(abs((node.i - self.target.i) * 3), abs((node.j - self.target.j) * 3))
