class Graph:
    # num_vertex represent the number of nodes.
    def __init__(self, num_vertex):
        self.adj_matrix = [[-1] * num_vertex for _ in range(num_vertex)]
        self.num_vertex = num_vertex

        # Mapping the node_number with the value as a (value, node_number) element
        self.vertices = {}

        # Store value of nodes to get it later
        self.vertices_list = [0] * num_vertex

    def set_vertex(self, node_number, value):
        # Check if node_number in [0, vertices] range
        if 0 <= node_number <= self.num_vertex:
            self.vertices[value] = node_number
            self.vertices_list[node_number] = value

    def set_edge(self, frm, to, weight):
        # Retrieves the node_number at its corresponding value
        frm = self.vertices[frm]
        to = self.vertices[to]
        self.adj_matrix[frm][to] = weight

        # Don't add the following in directed graphs
        self.adj_matrix[to][frm] = weight

    def get_vertex(self):
        return self.vertices_list

    def get_edges(self):
        edges = []
        for i in range(self.num_vertex):
            for j in range(self.num_vertex):
                if self.adj_matrix[i][j] != -1:
                    # Add first_node, second_node, weight
                    edges.append((self.vertices_list[i], self.vertices_list[j], self.adj_matrix[i][j]))

        return edges

    def get_matrix(self):
        return self.adj_matrix


G = Graph(6)
G.set_vertex(0, 'a')
G.set_vertex(1, 'b')
G.set_vertex(2, 'c')
G.set_vertex(3, 'd')
G.set_vertex(4, 'e')
G.set_vertex(5, 'f')
G.set_edge('a', 'e', 10)
G.set_edge('a', 'c', 20)
G.set_edge('c', 'b', 30)
G.set_edge('b', 'e', 40)
G.set_edge('e', 'd', 50)
G.set_edge('f', 'e', 60)

print("Vertices of Graph")
print(G.get_vertex())
print("Edges of Graph")
print(G.get_edges())
print("Adjacency Matrix of Graph")
print(G.get_matrix())
