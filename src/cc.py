"""
   Connected Components via DFS.
   Time:  O(V + E)
   Space: O(V)
"""


class CC:

    def __init__(self, graph):
        self._marked = [False] * graph.V
        self._id     = [0]     * graph.V
        self._count  = 0

        for v in range(graph.V):
            if not self._marked[v]:
                self._dfs(graph, v)
                self._count += 1

    def _dfs(self, graph, v):
        self._marked[v] = True
        self._id[v] = self._count
        for w in graph.adj[v]:
            if not self._marked[w]:
                self._dfs(graph, w)

    def connected(self, v, w):
        return self._id[v] == self._id[w]

    def id(self, v):
        return self._id[v]

    def count(self):
        return self._count

    def components(self, graph):
        """Return list of lists, each sub-list is the vertices of one component."""
        groups = [[] for _ in range(self._count)]
        for v in range(graph.V):
            groups[self._id[v]].append(v)
        return groups
