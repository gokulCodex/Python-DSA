graph={
    0:[2,3,4],
    1:[2,7],
    2:[5],
    3:[5,7],
    4:[7],
    5:[6],
    6:[7],
    7:[]
}

import numpy as np

def findAdjMat(graph):                  
    A=np.zeros((len(graph),len(graph)))
    for i in graph:
        for j in graph[i]:
            A[i,j]=1
    return A

def topsort(AMat):
    rows,cols=AMat.shape
    indegree={}
    topsortlist=[]
    for col in range(cols):
        indegree[col]=0
        for r in range(rows):
            if AMat[r,col]==1:
                indegree[col]+=1
    for i in range(rows):
        j=min([k for k in range(cols) if indegree[k]==0])
        topsortlist.append(j)
        indegree[j]-=1
        for k in range(cols):
            if AMat[j,k]==1:
                indegree[k]-=1
    return topsortlist

adj_matrix=findAdjMat(graph)
print(topsort(adj_matrix))

