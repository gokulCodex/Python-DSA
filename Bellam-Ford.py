graph={
    0:[(1,4),(2,1)],
    1:[(3,1)],
    2:[(1,2),(3,5)],
    3:[(4,3)],
    4:[]
}

def bellmanfordlist(graph,start):  #This can be used when there is negative weighted edges unlike Dijkstra's
    distance={}                    #There should be no negative cycles. Hence, it can detect negative cycles
    for v in graph.keys():
        distance[v]=float('inf')
    distance[start]=0
    for i in graph.keys():
        for u in graph.keys():
            for v,d in graph[u]:
                distance[v]=min(distance[v],distance[u]+d)
    return distance

print(bellmanfordlist(graph,0))