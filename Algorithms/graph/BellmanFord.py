class Graph:
    def __init__(self, vertices_size):
        self.vertices = vertices_size
        self.graph = []

    def add_edge(self, s, d, w):
        self.graph.append([s, d, w])

    def print_graph(self, weights):
        print("Vertex Distance From Source")
        for idx in range(self.vertices):
            print("%d \tis\t %d" % (idx, weights[idx]))

    def bellman_ford(self, src):

        # source node's weight 0 and remaining are INF
        weights = [float("Inf")] * self.vertices
        weights[src] = 0

        cycles = self.vertices - 1
        for idx in range(cycles):
            # for each cycle; we need to check all nodes
            for s, d, w in self.graph:
                if weights[s] != float("Inf") and weights[s] + w < weights[d]:
                    weights[d] = weights[s] + w

        # Assure there's no -ve cycle
        # Bcs if we find only one more cycle -> it's a -ve cycle
        for s, d, w in self.graph:
            if weights[s] != float("Inf") and weights[s] + w < weights[d]:
                print("Graph contains a negative cycle")
                return

        # print weight or distance to reach a vertex
        self.print_graph(weights)


g = Graph(5)
g.add_edge(0, 1, -1)
g.add_edge(0, 2, 4)
g.add_edge(1, 2, 3)
g.add_edge(1, 3, 2)
g.add_edge(1, 4, 2)
g.add_edge(3, 2, 5)
g.add_edge(3, 1, 1)
g.add_edge(4, 3, -3)

g.bellman_ford(0)
