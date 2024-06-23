graph={'a':['b','c'],
       'b':['a'],
       'c':['a','d','e'],
       'd':['c'],
       'e':['c']
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
    
def BFS(graph,start_node):        
    visited={}
    key_list=list(graph.keys())
    for key in key_list:
        visited[key]=False
    visited[start_node]=True
    q=Queue()
    q.addq(start_node)
    order=[]
    while not q.isempty():
        current=q.delq()
        order.append(current)
        for j in graph[current]:
            if not visited[j]:
                visited[j]=True
                q.addq(j)
    return order
