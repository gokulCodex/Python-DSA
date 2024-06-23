edges=[(0,1),(0,4),(1,2),(2,0),
       (3,4),(3,6),(4,0),(4,3),
       (4,7),(5,3),(5,7),
       (6,5),(7,4),(7,8),
       (8,5),(8,9),(9,8)]
import numpy as np
A=np.zeros((10,10))
for i in edges:
    A[i[0],i[1]]=1
def neighbours(AMat,i):
    nbrs=[]
    rows,columns=np.shape(AMat)
    for j in range(columns):
        if AMat[i,j]==1:
            nbrs.append(j)
    return nbrs
#print(neighbours(A,1))

class Queue:
    def __init__(self):
        self.queue=[]
    def isempty(self):
        return self.queue==[]
    def addq(self,v):
        self.queue.append(v)
    def delq(self):
        v=None
        if not self.isempty():
            v=self.queue[0]
            self.queue=self.queue[1:]
        return v
    def __str__(self):
        return str(self.queue)

def BFS(AMat,v):                       #BFS Algo
    rows,columns=np.shape(AMat)
    visited={}                         
    for i in range(rows):
        visited[i]=False
    q=Queue()
    visited[v]=True
    q.addq(v)
    #lis=[]
    while not q.isempty():
        current=q.delq()
        #lis.append(j)
        for k in neighbours(AMat,current):
            if not visited[k]:
                visited[k]=True
                q.addq(k)
    #print(lis)
    return visited