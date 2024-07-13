graph={
    0:[(1,10),(3,18)],
    1:[(0,10),(2,20),(3,6)],
    2:[(1,20),(4,8)],
    3:[(0,18),(1,6),(4,70)],
    4:[(2,8),(3,70)]
}

def kruskal(graph):
    edges,component,TE=[],{},[]
    for u in graph.keys():
        edges.extend([(d,u,v) for (v,d) in graph[u]])
        component[u]=u
    edges.sort()
    for (d,u,v) in edges:
        if component[u]!=component[v]:
            TE.append((u,v))
            c=component[u]
            for w in graph.keys():
                if component[w]==c:
                    component[w]=component[v]
    return TE