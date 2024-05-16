# This helps us in using infinity
import sys


class Graph:
    def __init__(self, vertices_size):
        self.vertices_size = vertices_size
        self.graph = [[0 for _column in range(self.vertices_size)] for _row in range(self.vertices_size)]

    def print_solution(self, weight):
        print("Vertex Distance from Source")
        for node in range(self.vertices_size):
            print(node, "to", weight[node])

    def min_distance(self, weights, visited_set):

        weight = sys.maxsize
        src_idx = None

        for idx in range(self.vertices_size):
            if weights[idx] < weight and visited_set[idx] is False:
                weight = weights[idx]
                src_idx = idx

        return src_idx

    def dijkstra(self, src):

        # This sys.maxsize represents big number lik INF
        weights = [sys.maxsize] * self.vertices_size
        weights[src] = 0
        visited_set = [False] * self.vertices_size

        for _ in range(self.vertices_size):
            # Find the vertex with the minimum distance from the source
            src = self.min_distance(weights, visited_set)
            visited_set[src] = True

            # Update distances to adjacent vertices
            for idx in range(self.vertices_size):
                if self.graph[src][idx] > 0 and visited_set[idx] is False and \
                        weights[idx] > weights[src] + self.graph[src][idx]:
                    weights[idx] = weights[src] + self.graph[src][idx]

        self.print_solution(weights)


g = Graph(9)

# This is how do we read the graph matrix
g.graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0],  # 0 --> 1 = 4 and 0 --> 7 = 8
           [4, 0, 8, 0, 0, 0, 0, 11, 0],  # 1 --> 0 = 4 and 1 --> 2 = 8 and 1 --> 7 = 11 ...
           [0, 8, 0, 7, 0, 4, 0, 0, 2],
           [0, 0, 7, 0, 9, 14, 0, 0, 0],
           [0, 0, 0, 9, 0, 10, 0, 0, 0],
           [0, 0, 4, 14, 10, 0, 2, 0, 0],
           [0, 0, 0, 0, 0, 2, 0, 1, 6],
           [8, 11, 0, 0, 0, 0, 1, 0, 7],
           [0, 0, 2, 0, 0, 0, 6, 7, 0]
           ]

g.dijkstra(0)
