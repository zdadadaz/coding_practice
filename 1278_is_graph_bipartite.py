class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        color = {}
        def dfs(node):
            que = [node]
            while que:
                cur = que.pop()
                for nei in graph[cur]:
                    if nei not in color:
                        color[nei] = 1 - color[cur]
                        que.append(nei)
                    elif color[nei] == color[cur]:
                        return False
            return True
                                        
        for node in range(n):
            if node not in color:
                color[node] = 0
                if not dfs(node):       
                    return False
        return True

    def isBipartite_recursion(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        color = {}
        def dfs(node):
            for nei in graph[node]:
                if nei not in color:
                    color[nei] = 1 - color[node]
                    if not dfs(nei):
                        return False
                elif color[nei] == color[node]:
                    return False
            return True
                                        
        for node in range(n):
            if node not in color:
                color[node] = 0
                if not dfs(node):       
                    return False
        return True