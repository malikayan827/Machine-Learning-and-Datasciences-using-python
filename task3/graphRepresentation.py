#graph datastructure representation using list in python


vertices = ['A', 'B', 'C', 'D', 'E', 'F', 'G']


graph = {vertex:[] for vertex in vertices}
graph['A'].extend(['B', 'E', 'C'])
graph['B'].extend(['D', 'E'])
graph['C'].extend(['F', 'G'])
graph['D'].extend(['E','B'])
graph['E'].extend(['B','A','D'])
graph['F'].extend(['C'])
graph['G'].extend(['C'])
#graph datastructure representation using list in python using 2D list
vertices = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
edges = [['A', 'B'], ['A', 'E'], ['A', 'C'], ['B', 'D'], ['B', 'E'], ['C', 'F'], ['C', 'G'], ['D', 'E'], ['D', 'B'], ['E', 'B'], ['E', 'A'], ['E', 'D'], ['F', 'C'], ['G', 'C']]
graph = {vertex:[] for vertex in vertices}
for edge in edges:
    graph[edge[0]].append(edge[1])
    graph[edge[1]].append(edge[0])
#graph datastructure representation using list in python using 2D list
vertices = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
edges = [['A', 'B'], ['A', 'E'], ['A', 'C'], ['B', 'D'], ['B', 'E'], ['C', 'F'], ['C', 'G'], ['D', 'E'], ['D', 'B'], ['E', 'B'], ['E', 'A'], ['E', 'D'], ['F', 'C'], ['G', 'C']]
graph = {vertex:[] for vertex in vertices}
for edge in edges:
    graph[edge[0]].append(edge[1])
    graph[edge[1]].append(edge[0])
#graph datastructure representation using list in python using 2D list
vertices = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
edges = [['A', 'B'], ['A', 'E'], ['A', 'C'], ['B', 'D'], ['B', 'E'], ['C', 'F'], ['C', 'G'], ['D', 'E'], ['D', 'B'], ['E', 'B'], ['E', 'A'], ['E', 'D'], ['F', 'C'], ['G', 'C']]
graph = {vertex:[] for vertex in vertices}
for edge in edges:
    graph[edge[0]].append(edge[1])
    graph[edge[1]].append(edge[0])
print(graph)   



















for vertex, neighbors in graph.items():
    print(f"{vertex}: {', '.join(neighbors)}")

