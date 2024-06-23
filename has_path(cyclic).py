graph={'a':['b','d','c'],   #undirected cyclic graph
       'b':['a'],
       'c':['a','d','e'],
       'd':['c','a'],
       'e':['c']
}
def has_path(graph,start,end,visited):
    if start==end:
        return True
    if start in visited:
        return False
    visited.append(start)            #visited keeps track of which all nodes have been visited
    for i in graph[start]:
        if has_path(graph,i,end,visited):
            return True
    return False

print(has_path(graph,'a','d',[]))
    