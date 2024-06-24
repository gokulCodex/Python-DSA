#using BFS for finding shortest path is better
graph={
    'w':['x','v'],
    'x':['w','y'],
    'y':['x','z'],
    'z':['y','v'],
    'v':['z','w']
}
class Queue:
    def __init__(self):
        self.queue=[]
    def isempty(self):
        return self.queue==[]
    def addq(self,v):
        self.queue.append(v)
    def delq(self):
        if not self.isempty():
            ele=self.queue[0]
            self.queue=self.queue[1:]
        return ele
    
def BFS_shortest_path(graph,start,end):        
    visited={}
    key_list=list(graph.keys())
    for key in key_list:
        visited[key]=False
    visited[start]=True
    q=Queue()
    q.addq((start,0))
    while not q.isempty():
        current=q.delq()          #note that current will be a tuple here holding the node position and shortest distance
        if current[0]==end:       #to that node from the starting node
            return current
        for j in graph[current[0]]:
            if not visited[j]:
                visited[j]=True
                q.addq((j,current[1]+1))
print(BFS_shortest_path(graph,'w','z'))         