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
    
def topo_sort(graph):
    indegree,toposortlist={},[]
    for u in graph.keys():
        indegree[u]=0
    for u in graph.keys():
        for v in graph[u]:
            indegree[v]+=1
    zerodegreeq=Queue()
    for u in graph.keys():
        if indegree[u]==0:
            zerodegreeq.addq(u)
    while not zerodegreeq.isempty():
        j=zerodegreeq.delq()
        toposortlist.append(j)
        indegree[j]-=1
        for k in graph[j]:
            indegree[k]-=1
            if indegree[k]==0:
                zerodegreeq.addq(k)
    return toposortlist
print(topo_sort(graph))