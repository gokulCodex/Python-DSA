import BFS       #importing the BFS.py for simplicity
graph={
    3:[],
    4:[6],
    6:[4,5,7,8],
    8:[6],
    7:[6],
    5:[6],
    1:[2],
    2:[1]
}
def counter(graph):                #Counts number of connected graph subsets in
    key_list=list(graph.keys())    #a given graph
    visited={}
    for key in key_list:
        visited[key]=False
    count=0
    for k in key_list:
        if not visited[k]:
            order=BFS.BFS(graph,k)
            for i in order:
                visited[i]=True
            count+=1
    return count

        

