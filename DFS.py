graph={'a':['b','c'],
       'b':['a'],
       'c':['a','d','e'],
       'd':['c'],
       'e':['c']
}

class Stack:
    def __init__(self):
        self.stack=[]
    def isempty(self):
        return self.stack==[]
    def adds(self,v):
        self.stack.append(v)
    def dels(self):
        if not self.isempty():
            ele=self.stack[-1]
            self.stack=self.stack[:-1]
        return ele
    
def DFS(graph,start_node):
    visited={}
    key_list=list(graph.keys())
    for key in key_list:
        visited[key]=False
    visited[start_node]=True
    s=Stack()
    s.adds(start_node)
    order=[]
    while not s.isempty():
        current=s.dels()
        order.append(current)
        for j in graph[current]:
            if not visited[j]:
                visited[j]=True
                s.adds(j)
    return order

print(DFS(graph,'a'))