"""
   Cycle detection in an undirected graph (DFS-based).

   Time complexity:  O(V + E) — each vertex and edge visited at most once.
   Space complexity: O(V)     — marked array, edge_to array, recursion stack
                                depth up to V in the worst case.
"""
import sys
sys.setrecursionlimit(10_000)


class Cycle:

    def __init__(self, graph):
        self._marked  = [False] * graph.V
        self._edge_to = [-1]    * graph.V
        self._cycle   = None

        for v in range(graph.V):
            if not self._marked[v]:
                self._dfs(graph, -1, v)

    def _dfs(self, graph, parent, v):
        self._marked[v] = True
        for w in graph.adj[v]:
            if self._cycle is not None:
                return
            if not self._marked[w]:
                self._edge_to[w] = v
                self._dfs(graph, v, w)
            elif w != parent:
                # Back-edge found: reconstruct cycle from v back to w
                path = []
                x = v
                while x != w:
                    path.append(x)
                    x = self._edge_to[x]
                path.append(w)   # append w (far end of cycle)
                path.reverse()   # path now starts at w
                path.append(w)   # close the cycle: end == start
                self._cycle = path

    def has_cycle(self):
        return self._cycle is not None

    def get_cycle(self):
        return self._cycle
