# Exercise 1

# a) True
# b) False
# c) True

# Exercise 2

class Graph:
    graph = dict()

    def add_edge(self, node, neighbour):
        if node not in self.graph:
            self.graph[node] = [neighbour]
        else:
            self.graph[node].append(neighbour)

    def print_graph(self):
        print(self.graph)

    def nodes_out_degree(self, n: int) -> list:
        degree = []

        for key in self.graph:
            if len(self.graph[key]) == n:
                degree.append(key)

        return degree

    def remove_edge(self, node1, node2):
        if node1 in self.graph and node2 in self.graph[node1]:
            self.graph[node1].remove(node2)

    def breadth_first_search(self, node):
        searched = [node]
        search_queue = [node]

        while search_queue:
            node = search_queue.pop(0)

            print(f'[ {node}', end=' ]')

            if node in self.graph:
                for neighbour in self.graph[node]:
                    if neighbour not in searched:
                        searched.append(neighbour)
                        search_queue.append(neighbour)


graph = Graph()
graph.add_edge('A', 'B')
graph.add_edge('A', 'C')
graph.add_edge('A', 'D')
graph.add_edge('B', 'A')
graph.add_edge('C', 'A')
graph.add_edge('B', 'C')
graph.add_edge('F', 'B')

graph.print_graph()
graph.remove_edge('A', 'D')
# print(graph.nodes_out_degree(2))
graph.print_graph()
