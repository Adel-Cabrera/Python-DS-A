graph1 = {
    'A' : ['B','S'],
    'B' : ['A'],
    'C' : ['D','E','F','S'],
    'D' : ['C'],
    'E' : ['C','H'],
    'F' : ['C','G'],
    'G' : ['F','S'],
    'H' : ['E','G'],
    'S' : ['A','C','G']
}

def deep_first(graph, node, visited_array):
    if node not in visited_array:
        visited_array.append(node)
        for n in graph[node]:
            deep_first(graph,n, visited_array)
    return visited_array

visited_array = deep_first(graph1,'A', [])
print(visited_array)
