# Graph Implementation
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


    # BFS Implementation
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

    # DFS implementation
    searched = []

    def depth_first_search(self, node):
        if node not in self.searched:

            print(f'[ {node} ',end=']')

            self.searched.append(node)
            if node in self.graph:
                for neighbour in self.graph[node]:
                    self.depth_first_search(neighbour)

def build_my_graph():
    my_graph = Graph()

    my_graph.add_edge(0, 1)
    my_graph.add_edge(0, 2)
    my_graph.add_edge(0, 3)
    my_graph.add_edge(1, 3)
    my_graph.add_edge(2, 3)
    my_graph.add_edge(3, 4)
    my_graph.add_edge(4, 1)

    print("BFS")
    my_graph.breadth_first_search(0)
    print('DFS')
    my_graph.depth_first_search(0)

build_my_graph()