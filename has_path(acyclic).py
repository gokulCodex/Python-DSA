graph={'a':['b','e'],          #Directed graph 
       'b':['g'],
       'c':['a'],
       'd':['b','f'],
       'e':['f'],
       'f':[],
       'g':[]
}
def has_path(graph,start,end):
    if start==end:
        return True
    for i in graph[start]:
        if has_path(graph,i,end):
            return True
    return False
print(has_path(graph,'a','d'))