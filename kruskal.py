class UnionFind:
    def __init__(self, nodes):
        self.parent = {node: node for node in nodes}
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    def union(self, x, y):
        self.parent[self.find(x)] = self.find(y)

def kruskal(graph):
    edges = sorted((cost, u, v) for u in graph for v, cost in graph[u])
    uf = UnionFind(graph.keys())
    mst = []
    for cost, u, v in edges:
        if uf.find(u) != uf.find(v):
            uf.union(u, v)
            mst.append((u, v, cost))
    return mst

n = int(input("Enter number of edges: "))
graph = {}
print("Enter edges (node1 node2 cost):")
for _ in range(n):
    u, v, cost = input().split()
    cost = int(cost)
    graph.setdefault(u, []).append((v, cost))
    graph.setdefault(v, []).append((u, cost))

print("Kruskal's MST:", kruskal(graph))
