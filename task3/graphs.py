class Graph:
    def __init__(self, num_nodes, edges):
        self.num_nodes = num_nodes
        self.data = [[] for _ in range(num_nodes)]
        self.node_names = {}  # A dictionary to map node names to integer indices

        # Assign integer indices to node names
        index_counter = 0
        for n1, n2 in edges:
            if n1 not in self.node_names:
                self.node_names[n1] = index_counter
                index_counter += 1
            if n2 not in self.node_names:
                self.node_names[n2] = index_counter
                index_counter += 1

        # Add edges using integer indices
        for n1, n2 in edges:
            index_n1 = self.node_names[n1]
            index_n2 = self.node_names[n2]
            self.data[index_n1].append(index_n2)
            self.data[index_n2].append(index_n1)
    

num_nodes = 7
edges = [('A', 'B'), ('A', 'E'), ('A', 'C'), ('B', 'E'),
         ('B', 'D'), ('C', 'F'), ('C', 'G')]

graph1 = Graph(num_nodes, edges)
# print(graph1.data)
