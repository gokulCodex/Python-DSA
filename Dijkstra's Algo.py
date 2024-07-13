graph={
    0:[(1,4),(2,1)],
    1:[(3,1)],
    2:[(1,2),(3,5)],
    3:[(4,3)],
    4:[]
}
 
def dijkstras(graph,start):
    distance,visited={},{}
    for v in graph.keys():
        distance[v]=float('inf')
        visited[v]=False
    distance[start]=0
    for u in graph.keys():
        nextd=min([distance[v] for v in graph.keys() if not visited[v]])
        nextvlist=[v for v in graph.keys() if (not visited[v]) and distance[v]==nextd]
        if nextvlist==[]:
            break
        nextv=min(nextvlist)
        visited[nextv]=True
        for v,d in graph[nextv]:
            if not visited[v]:
                distance[v]=min(distance[v],distance[nextv]+d)
    return distance

print(dijkstras(graph,0))

