import math

class Node:
    def __init__(self, state, parent, actions, heuristic, totalCost):
        self.state = state
        self.parent = parent
        self.actions = actions
        self.heuristic = heuristic
        self.totalCost = totalCost

def findMin(frontier):
    minNode = None
    minCost = float("inf")
    for node, (parent, cost) in frontier.items():
        if cost < minCost:
            minNode = node
            minCost = cost
    return minNode

def actionSequence(graph, initialState, goalState):
    sequence = []
    currentNode = goalState
    while currentNode != initialState:
        parent = graph[currentNode].parent
        for action, _ in graph[parent].actions:
            if action == currentNode:
                sequence.insert(0, action)
                break
        currentNode = parent
    return sequence

def calculateEuclideanDistance(node1, node2):
    x1, y1 = node1
    x2, y2 = node2
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

def solutionAstar(graph, initialState, goalState):
    frontier = {}
    explored = {}
    
    graph[initialState].totalCost = 0
    graph[initialState].heuristic = calculateEuclideanDistance(graph[initialState].heuristic, graph[goalState].heuristic)
    frontier[initialState] = (None, graph[initialState].totalCost + graph[initialState].heuristic)
    
    while frontier:
        currentNode = findMin(frontier)
        del frontier[currentNode]
        
        if currentNode == goalState:
            solution = actionSequence(graph, initialState, goalState)
            
            # Display heuristic values
            for state in graph:
                print(f"Heuristic for {state}: {graph[state].heuristic}")
            
            return solution
        
        explored[currentNode] = True
        
        for child, cost in graph[currentNode].actions:
            currentCost = graph[currentNode].totalCost + cost
            if child not in explored and (child not in frontier or currentCost < graph[child].totalCost):
                graph[child].parent = currentNode
                graph[child].totalCost = currentCost
                graph[child].heuristic = calculateEuclideanDistance(graph[child].heuristic, graph[goalState].heuristic)
                frontier[child] = (currentNode, currentCost + graph[child].heuristic)
    
    return []

graph = {
    "A": Node("A", None, [("F", 1)], (0, 0), 0),
    "B": Node("B", None, [("C", 1), ("G", 1)], (0, 2), 0),
    "C": Node("C", None, [("B", 1), ("D", 1)], (0, 3), 0),
    "D": Node("D", None, [("C", 1), ("E", 1)], (0, 4), 0),
    "E": Node("E", None, [("D", 1)], (0, 5), 0),
    "F": Node("F", None, [("A", 1), ("H", 1)], (1, 0), 0),
    "G": Node("G", None, [("B", 1), ("J", 1)], (1, 2), 0),
    "H": Node("H", None, [("F", 1), ("I", 1), ("M", 1)], (2, 0), 0),
    "I": Node("I", None, [("N", 1), ("J", 1)], (2, 1), 0),
    "J": Node("J", None, [("G", 1), ("I", 1)], (2, 2), 0),
    "K": Node("K", None, [("L", 1), ("P", 1)], (2, 4), 0),
    "L": Node("L", None, [("K", 1), ("Q", 1)], (2, 5), 0),
    "M": Node("M", None, [("H", 1), ("N", 1), ("R", 1)], (3, 0), 0),
    "N": Node("N", None, [("I", 1), ("M", 1), ("S", 1)], (3, 1), 0),
    "O": Node("O", None, [("P", 1), ("U", 1)], (3, 3), 0),
    "P": Node("P", None, [("Q", 1), ("O", 1)], (3, 4), 0),
    "Q": Node("Q", None, [("L", 1), ("P", 1), ("V", 1)], (3, 5), 0),
    "R": Node("R", None, [("M", 1), ("S", 1)], (4, 0), 0),
    "S": Node("S", None, [("N", 1), ("R", 1), ("T", 1)], (4, 1), 0),
    "T": Node("T", None, [("S", 1), ("U", 1), ("W", 1)], (4, 2), 0),
    "U": Node("U", None, [("O", 1), ("T", 1)], (4, 3), 0),
    "V": Node("V", None, [("Q", 1), ("Y", 1)], (4, 5), 0),
    "W": Node("W", None, [("T", 1)], (5, 2), 0),
    "X": Node("X", None, [("Y", 1)], (5, 4), 0),
    "Y": Node("Y", None, [("V", 1), ("X", 1)], (5, 5), 0),
}
initialState = "A"
goalState = "Y"

solution = solutionAstar(graph, initialState, goalState)
print("Solution:", solution)