from collections import defaultdict, deque

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def bfs(self, start):
        visited = set()
        queue = deque([start])
        visited.add(start)
        while queue:
            v = queue.popleft()
            print(v, end=' ')
            for neighbor in self.graph[v]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

# Input
g = Graph()
n = int(input("Enter number of edges: "))
print("Enter edges (u v):")
for _ in range(n):
    u, v = map(int, input().split())
    g.add_edge(u, v)

start = int(input("Enter starting node: "))
print("BFS traversal:")
g.bfs(start)