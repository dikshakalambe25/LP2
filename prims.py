def prim(graph, start):
    mst = []
    visited = {start}
    edges = [(weight, start, to) for to, weight in graph[start]]

    while edges:
        edges.sort()
        weight, frm, to = edges.pop(0)
        if to not in visited:
            visited.add(to)
            mst.append((frm, to, weight))
            edges.extend((w, to, nxt) for nxt, w in graph[to] if nxt not in visited)
    return mst

# User input for graph
n = int(input("Enter number of edges: "))
graph = {}
for _ in range(n):
    u, v, cost = input().split()
    cost = int(cost)
    graph.setdefault(u, []).append((v, cost))
    graph.setdefault(v, []).append((u, cost))

start = input("Enter start node: ")
print("Prim's MST:", prim(graph, start))