class Node:
    def __init__(self, state, parent, actions, totalcost):
        self.state = state
        self.parent = parent
        self.actions = actions
        self.totalcost = totalcost
def bfs(visited, graph, start, goal):
    visited.append(start)
    queue = [start]

    while queue:
        current = queue.pop(0)
        print(current, end=" ")

        if current == goal:
            return  # Stop when the goal is reached

        for neighbour in graph[current].actions:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)

# Initialize the visited list
visited = []

# Define the graph
romania_TSP = {
    "Arad": Node("Arad", None, ["Zerind", "Sibiu", "Timisoara"], None),
    "Zerind": Node("Zerind", None, ["Arad", "Oradea"], None),
    "Oradea": Node("Oradea", None, ["Zerind", "Sibiu"], None),
    "Sibiu": Node("Sibiu", None, ["Arad", "Oradea", "Fagaras", "Rimnicu Vilcea"], None),
    "Timisoara": Node("Timisoara", None, ["Arad", "Lugoj"], None),
    "Lugoj": Node("Lugoj", None, ["Timisoara", "Mehadia"], None),
    "Mehadia": Node("Mehadia", None, ["Lugoj", "Drobeta"], None),
    "Drobeta": Node("Drobeta", None, ["Mehadia", "Craiova"], None),
    "Craiova": Node("Craiova", None, ["Drobeta", "Rimnicu Vilcea", "Pitesti"], None),
    "Rimnicu Vilcea": Node(
        "Rimnicu Vilcea", None, ["Sibiu", "Craiova", "Pitesti"], None
    ),
    "Fagaras": Node("Fagaras", None, ["Sibiu", "Bucharest"], None),
    "Pitesti": Node("Pitesti", None, ["Rimnicu Vilcea", "Craiova", "Bucharest"], None),
    "Bucharest": Node(
        "Bucharest", None, ["Fagaras", "Pitesti", "Giurgiu", "Urziceni"], None
    ),
    "Giurgiu": Node("Giurgiu", None, ["Bucharest"], None),
    "Urziceni": Node("Urziceni", None, ["Bucharest", "Hirsova", "Vaslui"], None),
    "Hirsova": Node("Hirsova", None, ["Urziceni", "Eforie"], None),
    "Eforie": Node("Eforie", None, ["Hirsova"], None),
    "Vaslui": Node("Vaslui", None, ["Urziceni", "Iasi"], None),
    "Iasi": Node("Iasi", None, ["Vaslui", "Neamt"], None),
    "Neamt": Node("Neamt", None, ["Iasi"], None),
}

# Start and goal nodes
start_node = "Bucharest"
goal_node = "Arad"

# Perform BFS
print("BFS path from", start_node, "to", goal_node, "is:")
bfs(visited, romania_TSP, start_node, goal_node)
