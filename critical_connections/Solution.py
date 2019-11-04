from collections import defaultdict

class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        graph = defaultdict(list)
        for v in connections:
            graph[v[0]].append(v[1])
            graph[v[1]].append(v[0])

        ids = [None for i in range(n)]
        low = [None for i in range(n)]

        res = []
        self.cur = 0

        def dfs(i, parent):
            if ids[i] is None:
                ids[i] = self.cur
                low[i] = self.cur
                self.cur += 1
                for j in graph[i]:
                    if ids[j] is None:
                        dfs(j, i)

                if parent is not None:
                    l = min([low[i] for i in graph[i] if i != parent] + [low[i]])
                else:
                    l = min(low[i] for i in graph[i] + [low[i]])
                low[i] = l

        dfs(0, None)

        for v in connections:
            if low[v[0]] > ids[v[1]] or low[v[1]] > ids[v[0]]:
                res.append(v)
        return res