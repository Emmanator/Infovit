# Exercise 1

# a) True
# b) False
# c) False

# Exercise 2

class Graph:
    graph = dict()

    def add_edge(self, node, neighbour):
        if node in self.graph:
            self.graph[node] = [neighbour]

        else:
            self.graph[node].append(neighbour)

    def print_graph(self):
        print(self.graph)

    def nodes_out_degree(self, n):
        return

graph = Graph()
graph.add_edge('A', 'B')
graph.add_edge('A', 'C')
graph.add_edge('B', 'A')
graph.add_edge('C', 'A')
graph.add_edge('B', 'C')
graph.add_edge('F', 'B')
