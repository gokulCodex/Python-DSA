graph={
    0:[(1,10),(3,18)],
    1:[(0,10),(2,20),(3,6)],
    2:[(1,20),(4,8)],
    3:[(0,18),(1,6),(4,70)],
    4:[(2,8),(3,70)]
}

def prim(graph):
    min_cost = 0
    visited = [False] * len(graph)
    min_heap = [(0, 0)]  
    
    while min_heap:
        min_heap.sort()
        cost, node = min_heap.pop(0)
        if visited[node]:
            continue
        min_cost += cost
        visited[node] = True
        for neighbor, weight in graph[node]:
            if not visited[neighbor]:
                min_heap.append((weight, neighbor))
    
    return min_cost

print(prim(graph))
    

