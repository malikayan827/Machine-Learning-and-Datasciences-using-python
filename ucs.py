class Node:
    def __init__(self, state, parent, actions, totalcost):
        self.state = state
        self.parent = parent
        self.actions = actions
        self.totalcost = totalcost

graph1 = {
    "Arad": Node("Arad", None, [("Zerind", 75), ("Sibiu", 140), ("Timisoara", 118)], 0),
    "Zerind": Node("Zerind", None, [("Arad", 75), ("Oradea", 71)], 0),
    "Oradea": Node("Oradea", None, [("Zerind", 71), ("Sibiu", 151)], 0),
    "Sibiu": Node("Sibiu", None, [("Arad", 140), ("Oradea", 151), ("Fagaras", 99), ("Rimnicu Vilcea", 80)], 0),
    "Timisoara": Node("Timisoara", None, [("Arad", 118), ("Lugoj", 111)], 0),
    "Lugoj": Node("Lugoj", None, [("Timisoara", 111), ("Mehadia", 70)], 0),
    "Mehadia": Node("Mehadia", None, [("Lugoj", 70), ("Drobeta", 75)], 0),
    "Drobeta": Node("Drobeta", None, [("Mehadia", 75), ("Craiova", 120)], 0),
    "Craiova": Node("Craiova", None, [("Drobeta", 120), ("Rimnicu Vilcea", 146), ("Pitesti", 138)], 0),
    "Rimnicu Vilcea": Node("Rimnicu Vilcea", None, [("Sibiu", 80), ("Craiova", 146), ("Pitesti", 97)], 0),
    "Fagaras": Node("Fagaras", None, [("Sibiu", 99), ("Bucharest", 211)], 0),
    "Pitesti": Node("Pitesti", None, [("Rimnicu Vilcea", 97), ("Craiova", 138), ("Bucharest", 101)], 0),
    "Bucharest": Node("Bucharest", None, [("Fagaras", 211), ("Pitesti", 101), ("Giurgiu", 90), ("Urziceni", 85)], 0),
    "Giurgiu": Node("Giurgiu", None, [("Bucharest", 90)], 0),
    "Urziceni": Node("Urziceni", None, [("Bucharest", 85), ("Hirsova", 98), ("Vaslui", 142)], 0),
    "Hirsova": Node("Hirsova", None, [("Urziceni", 98), ("Eforie", 86)], 0),
    "Eforie": Node("Eforie", None, [("Hirsova", 86)], 0),
    "Vaslui": Node("Vaslui", None, [("Urziceni", 142), ("Iasi", 92)], 0),
    "Iasi": Node("Iasi", None, [("Vaslui", 92), ("Neamt", 87)], 0),
    "Neamt": Node("Neamt", None, [("Iasi", 87)], 0),
}

import math

def findMin(frontier):
    min_cost = math.inf
    node = ''
    for n in frontier:
        if frontier[n][1] < min_cost:
            min_cost = frontier[n][1]
            node = n
    return node

def actionSequence(graph, initialstate, goalstate):
    solution = [goalstate]
    current_parent = graph[goalstate].parent
    while current_parent is not None:
        solution.append(current_parent)
        current_parent = graph[current_parent].parent
    solution.reverse()
    return solution

def UCS(graph):
    initialState = "Arad"
    goalState = "Bucharest"
    frontier=dict()
    frontier[initialState]=(None,0)
    explored=[]
    while frontier:
        currentNode=findMin(frontier)
        del frontier[currentNode]
        if graph[currentNode].state == goalState:
            return actionSequence(graph, initialState, goalState)

        explored.append(currentNode)
        for child in graph[currentNode].actions:
            currentCost = child[1] + graph[currentNode].totalCost
            if child[0] not in explored and child[0] not in frontier:
                graph[child[0]].parent = currentNode
                graph[child[0]].totalCost = currentCost
                frontier[child[0]] = (graph[child[0]].parent, graph[child[0]].totalCost)
            elif child[0] in frontier and frontier[child[0]][1]>currentCost:
                    frontier[child[0]] = (currentNode, currentCost)
                    graph[child[0]].parent = frontier[child[0]][0]
                    graph[child[0]].totalCost = frontier[child[0]][1]

   
solution = UCS(graph1)
print(solution)
