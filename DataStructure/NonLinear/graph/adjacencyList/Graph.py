class AdjNode:
    def __init__(self, data):
        self.vertex = data
        self.next = None


class Graph:
    def __init__(self, vertices):
        self.vert_size = vertices
        self.graph = [None] * self.vert_size

    def add_edge(self, source, destination):
        node = AdjNode(destination)
        # Link it with source vertex as the head of linked list
        node.next = self.graph[source]
        self.graph[source] = node

        # We continue in undirected edges
        node = AdjNode(source)
        node.next = self.graph[destination]
        self.graph[destination] = node

    def print_graph(self):
        for vertex in range(self.vert_size):
            print("Adjacency List of vertex {}\n head".format(vertex), end=" ")
            current = self.graph[vertex]
            while current:
                print("-> {}".format(current.vertex), end=" ")
                current = current.next
            print("\n")


# Executes when the script is run as the main program.
if __name__ == "__main__":
    vertices_size = 5
    graph = Graph(vertices_size)
    graph.add_edge(0, 1)
    graph.add_edge(0, 4)
    graph.add_edge(1, 2)
    graph.add_edge(1, 3)
    graph.add_edge(1, 4)
    graph.add_edge(2, 3)
    graph.add_edge(3, 4)

    graph.print_graph()
