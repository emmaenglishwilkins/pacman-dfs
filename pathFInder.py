import numpy as np
vertexs = 'abcde'

edges = 'ab ac ba bd de'.split(' ')

def raiseto(m, times: int):
    result = m
    for i in range(times - 1):
        result = np.dot(result, m)
    return result

def make(vertexs, edges):
    d = {}
    for i, v in enumerate(vertexs):
        d[v] = i
    m = []
    for x in range(len(vertexs)):
        row = []
        for y in range(len(vertexs)):
            row.append(0)
        m.append(row)
    for edge in edges:
        if len(edge) < 2:
            continue
        m[d[edge[0]]][d[edge[1]]] +=1
    return np.array(m)

def find_path(m: np.array, origin, target, vertexs):
    name_to_index = {v: i for i, v in enumerate(vertexs)}
    index_to_name = {i: v for i, v in enumerate(vertexs)}

    visited = set()
    origin_index = name_to_index[origin] # index of origin vertex
    inital_path = [origin] # inital path containing only the origin vertex 
    queue = [(origin_index, inital_path)] # list of tuples (node_index, path_so_far)


    while queue: 
        current_index, path = queue[0]
        queue = queue[1:] # pops the first element of the queue

        if index_to_name[current_index] == target:
            return path 
        if current_index in visited: 
            continue
        visited.add(current_index)

        for neighbor_index, connected in enumerate(m[current_index]):
            if connected and neighbor_index not in visited:
                new_path = path + [index_to_name[neighbor_index]]
                queue.append((neighbor_index, new_path))

    return None

m = make(vertexs, edges)
print("matrix")
print(m)
path = find_path(m, 'a', 'e', vertexs)
print("path from a to e", path)