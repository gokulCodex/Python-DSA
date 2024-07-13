graph={'a':['b','c'],
       'b':['a','d'],
       'c':['a','d','e'],
       'd':['b','c'],
       'e':['c']
}

def findAllPaths(graph, start, end):                 #A function that returns a list of lists of evry possible paths 
    def dfs(current, path):                          #from start to end
        path.append(current)
        if current == end:
            all_paths.append(list(path))
        else:
            for neighbor in graph[current]:
                if neighbor not in path:             #Prevent cycles
                    dfs(neighbor, path)
        path.pop() 
    all_paths = []
    dfs(start, [])
    return all_paths

print(findAllPaths(graph,'a','d'))