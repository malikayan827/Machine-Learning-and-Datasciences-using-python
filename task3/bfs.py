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

    def __repr__(self):
        return "\n".join(["{}:{}".format(n, neighbors) for n, neighbors in enumerate(self.data)])

    def __str__(self):
        return repr(self)

num_nodes = 7
edges = [('A', 'B'), ('A', 'E'), ('A', 'C'), ('B', 'E'),
         ('B', 'D'), ('C', 'F'), ('C', 'G')]

graph1 = Graph(num_nodes, edges)
print(graph1.data)

def bfs(graph, root_node_name):
    if root_node_name not in graph.node_names:
        print(f"Node '{root_node_name}' not found in the graph.")
        return []

    root_node_index = graph.node_names[root_node_name]
    queue = []
    discovered = [False] * len(graph.data)
    discovered[root_node_index] = True
    queue.append(root_node_index)
    result = []

    while queue:
        current = queue.pop(0)
        result.append(current)

        for neighbor in graph.data[current]:
            if not discovered[neighbor]:
                discovered[neighbor] = True
                queue.append(neighbor)

    # Convert integer indices back to node names for the result
    result_node_names = [node_name for node_name, node_index in graph.node_names.items() if node_index in result]
    return result_node_names

bfs_result = bfs(graph1, 'A')
print(bfs_result)
