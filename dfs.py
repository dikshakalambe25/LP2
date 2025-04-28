from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def dfs(self, v, visited=None):
        if visited is None:
            visited = set()
        visited.add(v)
        print(v, end=' ')
        for neighbor in self.graph[v]:
            if neighbor not in visited:
                self.dfs(neighbor, visited)

g = Graph()
n = int(input("Enter number of edges: "))
print("Enter edges (u v):")
for _ in range(n):
    u, v = map(int, input().split())
    g.add_edge(u, v)

start = int(input("Enter starting node: "))
print("DFS traversal:")
g.dfs(start)