from collections import defaultdict
import sys

# Increase recursion depth for deep trees
sys.setrecursionlimit(200000)

class Solution(object):
    def minEdgeReversals(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append((v, 0))
            adj[v].append((u, 1))

        ans = [0] * n

        def dfs_root(u, p):
            total_cost = 0
            for v, cost in adj[u]:
                if v != p:
                    total_cost += cost + dfs_root(v, u)
            return total_cost

        ans[0] = dfs_root(0, -1)

        def dfs_reroot(u, p):
            for v, cost in adj[u]:
                if v != p:
                    ans[v] = ans[u] + (1 if cost == 0 else -1)
                    dfs_reroot(v, u)

        dfs_reroot(0, -1)
        return ans