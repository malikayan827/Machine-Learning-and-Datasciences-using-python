#graph using nodes and classes
class Node:
    def __init__(self, state, parent, action, cost):
        self.state = state
        self.parent = parent  # Store neighbors as a list
        self.action = action
        self.cost = cost

graph1 = {
    'S': Node('S', ['P', 'E', 'D'], None, 0),
    'P': Node('P', ['S', 'Q', 'H'], None, 0),
    'E': Node('E', ['P', 'H'], None, 0),
    'D': Node('D', ['S', 'C', 'B'], None, 0),
    'Q': Node('Q', ['P', 'H'], None, 0),
    'H': Node('H', ['E', 'P', 'Q'], None, 0),
    'R': Node('R', ['E', 'F'], None, 0),
    'C': Node('C', ['D'], None, 0),
    'B': Node('B', ['D', 'A'], None, 0),
    'F': Node('F', ['R', 'G'], None, 0),
    'G': Node('G', ['F'], None, 0),
    'A': Node('A', ['B', 'C'], None, 0),
}

graph2 = {
    'A': Node('A', ['B', 'C', 'D', 'E'], None, 0),
    'B': Node('B', ['A', 'D', 'E'], None, 0),
    'C': Node('C', ['A', 'G', 'F'], None, 0),
    'D': Node('D', ['A', 'B', 'E'], None, 0),
    'E': Node('E', ['A', 'B', 'D'], None, 0),
    'F': Node('F', ['C'], None, 0),
    'G': Node('G', ['C'], None, 0),
}

# def print_graph(graph):
#     for node in graph:
#         print(f"{node}: {graph[node].parent}")

# print_graph(graph1) 
# Queue implementation using list
class Queue:
    def __init__(self):
        self.queue = []
    def enqueue(self, node):
        self.queue.append(node)
    def dequeue(self):
        if self.is_empty():
            return None
        else:
            return self.queue.pop(0)
    def is_empty(self):
        return len(self.queue) == 0
    def size(self):
        return len(self.queue)
    def front(self):
        if self.is_empty():
            return None
        else:
            return self.queue[0]
    def rear(self):
        if self.is_empty():
            return None
        else:
            return self.queue[-1]
    def print_queue(self):
        print("Queue: ", end = '')
        for node in self.queue:
            print(node.state, end = ' ')
        print()
# defining bfs function

def bfs(graph, start):
    front = Queue()
    front.enqueue(start)
    visited = set()  # Use a set for faster membership testing
    
    while not front.is_empty():
        node = front.dequeue()
        visited.add(node)
        for neighbor in graph[node].state:
            if neighbor not in visited:
                front.enqueue(neighbor)
                graph[neighbor].parent = node  # Store the parent while exploring
                
    return visited

def actionSequence(graph, start, goal):
    if goal not in graph:
        return []  # Return an empty list if the goal is not reachable
    
    solution = [goal]
    currentParent = graph[goal].parent
    while currentParent is not None:
        solution.append(currentParent)
        currentParent = graph[currentParent].parent
    solution.reverse()
    return solution

# Print the BFS traversal
bfs_traversal = bfs(graph1, 'S')
print("BFS Traversal of graph1:", bfs_traversal)

bfs_traversal = bfs(graph2, 'A')
print("BFS Traversal of graph2:", bfs_traversal)
    



