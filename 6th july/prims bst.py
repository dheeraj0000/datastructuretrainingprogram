import heapq

def print(graph,start):
    parent={}
    weights={}
    queue={}
    visited=set()
    for vertex in graph:
        weight[vertex]=99999
    weight[start]=0
    heap.heappush(queue,(0,start))
    
    while len(queue)!=0:
        cur_weight,cur_node=heapq.heapop(queue)
        if cur_node in visited:
            continue
        for weight,node in graph[cur_node]:
            #print(weight,node)
            if node not in visited and weight<weight[node]:
                weight[node]=weight
                parent[node]=cur_node
                heapq.heappush(queue,(weight,node))
            visited.add(cur_node)
        

graph={
    'A':[(1,'0'),(3,'E')],
    'B':[(1,'A'),(2,'E'),(1,'D'),(4,'c')],
    'C':[(4,'B'),(1,'D')],
    'D':[(1,'B'),(1,'c'),(2,'E')]
    }

