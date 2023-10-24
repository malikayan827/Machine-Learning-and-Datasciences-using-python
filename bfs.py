class Node:
    def __init__(self,state,parent,actions,totalCost):
        self.state=state
        self.parent=parent
        self.actions=actions
        self.totalCost=totalCost

graph={'A':Node('A',None,['B','C','E'],None),
       'B':Node('B',None,['A','D','E'],None),
       'C':Node('C',None,['A','F','G'],None),
       'D':Node('D',None,['B','E'],None),
       'E':Node('E',None,['B','A','D'],None),
       'F':Node('F',None,['C'],None),
       'G':Node('G',None,['C'],None),
       }
graph1={
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
graph2 = {
        "G": Node("G", None, ["5"], None),
        "1": Node("1", None, ["2", "7"], None),
        "2": Node("2", None, ["1", "3"], None),
        "3": Node("3", None, ["2", "4"], None),
        "4": Node("4", None, ["3", "5"], None),
        "5": Node("5", None, ["G", "4", "6"], None),
        "6": Node("6", None, ["5", "8"], None),
        "7": Node("7", None, ["1", "9"], None),
        "8": Node("8", None, ["6", "12"], None),
        "9": Node("9", None, ["7", "13"], None),
        "10": Node("10", None, ["14"], None),
        "11": Node("11", None, ["12"], None),
        "12": Node("12", None, ["11", "8", "15"], None),
        "13": Node("13", None, ["9", "16"], None),
        "14": Node("14", None, ["10", "17"], None),
        "15": Node("15", None, ["12", "19"], None),
        "16": Node("16", None, ["13", "20"], None),
        "17": Node("17", None, ["14", "22"], None),
        "18": Node("18", None, ["24", "19"], None),
        "19": Node("19", None, ["15", "18", "25"], None),
        "20": Node("20", None, ["16", "21"], None),
        "21": Node("21", None, ["20", "22"], None),
        "22": Node("22", None, ["17", "21", "23"], None),
        "23": Node("23", None, ["22", "24"], None),
        "24": Node("24", None, ["23", "25", "18"], None),
        "25": Node("25", None, ["19", "24"], None),
    }

def actionSequence(graph,initialState,goalState):
   solution=[goalState]
   currentParent=graph[goalState].parent
   while currentParent!=None:
      solution.append(currentParent)
      currentParent=graph[currentParent].parent
   solution.reverse()
   return solution
# def actionSequence(goalstate,initialstate,graph):
#    solution=[goalstate]
#    currentparent=graph[goalstate].parent
#    while currentparent!=None:
#       solution.append(currentparent)
#       currentparent=graph[currentparent].parent
#    solution.reverse()
#    return solution  
# def bfs(graph):
#     initialstate='Arad'
#     goalstate='Bucharest'
#     frontier=[initialstate]
#     explored=[]
#     while len(frontier):
#      currentnode=frontier.pop(0)
#      explored.append(currentnode)
#      for child in graph[currentnode].actions:
#         if child not in frontier and child not in explored:
#            graph[child].parent=currentnode
#            if graph[child].state==goalstate:
#               return actionSequence(graph,initialstate,goalstate)
#            frontier.append(child)
def bfs(graph):
    initialstate='Arad'
    goalstate='Bucharest'
    frontier=[initialstate]
    explored=[]
    while len(frontier)!=0:
        currentnode=frontier.pop(0)
        explored.append(currentnode)
        for child in graph[currentnode].actions:
            if child not in explored and child not in frontier:
                graph[child].parent=currentnode
                if graph[child].state==goalstate:
                    return actionSequence(graph,initialstate,goalstate)
                frontier.append(child)




solution=bfs(graph2)
print(solution)
