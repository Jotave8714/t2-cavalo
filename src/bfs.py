"""
   Breadth-First Search for shortest path in an unweighted graph.
   Time:  O(V + E)
   Space: O(V)
"""
from collections import deque


class BFS:
    INFINITY = float("inf")

    def __init__(self, graph, source):
        self._dist_to = [self.INFINITY] * graph.V
        self._edge_to = [-1] * graph.V
        self._dist_to[source] = 0
        self._bfs(graph, source)

    def _bfs(self, graph, s):
        queue = deque([s])
        while queue:
            v = queue.popleft()
            for w in graph.adj[v]:
                if self._dist_to[w] == self.INFINITY:
                    self._dist_to[w] = self._dist_to[v] + 1
                    self._edge_to[w] = v
                    queue.append(w)

    def dist_to(self, v):
        return self._dist_to[v]

    def has_path_to(self, v):
        return self._dist_to[v] != self.INFINITY

    def path_to(self, v):
        if not self.has_path_to(v):
            return None
        path = []
        x = v
        while self._edge_to[x] != -1:
            path.append(x)
            x = self._edge_to[x]
        path.append(x)
        path.reverse()
        return path
