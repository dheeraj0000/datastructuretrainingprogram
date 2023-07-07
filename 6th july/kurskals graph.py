def kruskals(graph):
    edge_list = []
    for source in graph:
        for edge in graph[source]:
            weight, dest = edge
            edge_list.append((weight, source, dest))
    edge_list.sort()
    print(*edge_list, sep="\n")
    parents = {}
    for vertex in graph:
        parents[vertex] = vertex
    print(parents)
    mst = []

    def find_parent(vertex):
        if parents[vertex] != vertex:
            parents[vertex] = find_parent(parents[vertex])
        return parents[vertex]

    for edge in edge_list:
        weight, source, dest = edge
        if find_parent(source) != find_parent(dest):
            mst.append(edge)
            parents[find_parent(source)] = find_parent(dest)
    return mst


graph = {
    'A': [(1, 'B'), (3, 'E')],
    'B': [(1, 'A'), (2, 'E'), (1, 'D'), (4, 'C')],
    'C': [(4, 'B'), (1, 'D')],
    'D': [(1, 'B'), (1, 'C'), (2, 'E')],
    'E': [(3, 'A'), (2, 'B'), (2, 'D')]
}

mst = kruskals(graph)
print(mst)