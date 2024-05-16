class Graph:

    # vertices is the number of vertex we've
    def __init__(self, vertices):
        self.vertices = vertices

        # Initialize an empty list to store the edges
        self.edges = []

    # we add source node, destination node, and weight
    def add_edge(self, s, d, w):
        self.edges.append([s, d, w])

    # So we search recursively until we find the root of the node
    def find(self, parent, node):
        if parent[node] == node:
            return node
        return self.find(parent, parent[node])

    # This method is used to merge edges
    def union(self, parent, rank, source, destination):
        s_parent = self.find(parent, source)
        d_parent = self.find(parent, destination)

        if rank[s_parent] < rank[d_parent]:
            parent[s_parent] = d_parent
        elif rank[s_parent] > rank[d_parent]:
            parent[d_parent] = s_parent

        else:
            parent[d_parent] = s_parent
            rank[s_parent] += 1

    # MST: minimum spanning tree
    def kruskal_mst(self):

        # Initialize an empty list to store the MST edges
        mst = []

        # Initialize lists to keep track of parent nodes and ranks of each node
        parent = [i for i in range(self.vertices)]
        rank = [0] * self.vertices

        # Sort the edges based on their weights
        self.edges.sort(key=lambda edge: edge[2])

        # Iterate through the sorted edges
        for edge in self.edges:
            s, d, w = edge
            s_parent = self.find(parent, s)
            d_parent = self.find(parent, d)

            # Add the edge to the MST if it does not create a cycl
            if s_parent != d_parent:
                mst.append([s, d, w])
                self.union(parent, rank, s_parent, d_parent)

        # print the edges
        print("The following are constructed edges in MST")
        for s, d, weight in mst:
            print("%d -- %d == %d" % (s, d, weight))


g = Graph(4)
g.add_edge(0, 1, 10)
g.add_edge(0, 2, 6)
g.add_edge(0, 3, 5)
g.add_edge(1, 3, 15)
g.add_edge(2, 3, 4)

g.kruskal_mst()
