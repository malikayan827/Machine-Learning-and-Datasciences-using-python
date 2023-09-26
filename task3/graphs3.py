graph={
    'A':['B','E','C'],
    'B':['A','E','D'],
    'C':['A','F','G'],
    'D':['B','E'],
    'E':['A','B','D'],
    'F':['C'],
    'G':['C']
}
graph2={
    'A':[],
    'B':['A'],
    'C':['A'],
    'D':['B','C'],
    'E':['H','R'],
    'F':['G'],
    'G':[],
    'H':['P','Q'],
    'S':['D','E','P'],
    'P':['Q'],
    'Q':[],
    'R':['F']
}
romania_TSP = {
    "Arad": ["Zerind", "Sibiu", "Timisoara"],
    "Zerind": ["Arad", "Oradea"],
    "Oradea": ["Zerind", "Sibiu"],
    "Sibiu": ["Arad", "Oradea", "Fagaras", "Rimnicu Vilcea"],
    "Timisoara": ["Arad", "Lugoj"],
    "Lugoj": ["Timisoara", "Mehadia"],
    "Mehadia": ["Lugoj", "Drobeta"],
    "Drobeta": ["Mehadia", "Craiova"],
    "Craiova": ["Drobeta", "Rimnicu Vilcea", "Pitesti"],
    "Rimnicu Vilcea": ["Sibiu", "Craiova", "Pitesti"],
    "Fagaras": ["Sibiu", "Bucharest"],
    "Pitesti": ["Rimnicu Vilcea", "Craiova", "Bucharest"],
    "Bucharest": ["Fagaras", "Pitesti", "Giurgiu", "Urziceni"],
    "Giurgiu": ["Bucharest"],
    "Urziceni": ["Bucharest", "Hirsova", "Vaslui"],
    "Hirsova": ["Urziceni", "Eforie"],
    "Eforie": ["Hirsova"],
    "Vaslui": ["Urziceni", "Iasi"],
    "Iasi": ["Vaslui", "Neamt"],
    "Neamt": ["Iasi"],
}

#function to perform bfs
visited=[]
visited2=[]
queue=[]
def bfs(visited,graph,node):
    visited.append(node)
    queue.append(node)
    while queue:
        s=queue.pop(0)
        print(s,end=" ")

        for neighbour in graph[s]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)
def bfs2(visited,graph,node,goal):
    visited.append(node)
    queue.append(node)
    while queue:
        s=queue.pop(0)
        print(s,end=" ")

        if s == goal:
            return  
        
        for neighbour in graph[s]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)
#function to perform dfs
def dfs(visited, graph, node):
    if node not in visited:
        print (node)
        visited.append(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)
print("Following is the depts-First Search")
# Driver Code
dfs(visited, graph, 'A')
#driver code
print("Following is the Breadth-First Search")
bfs(visited, graph, 'A')
bfs2(visited,romania_TSP,'Bucharest',"Arad")