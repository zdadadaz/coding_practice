class Solution:
    def calcEquation(self, equations, values, queries):
        # dfs with recursion version
        def divide(x, y, visited):
            if x == y: 
                return 1.0
            visited.add(x)
            for n in g[x]:
                if n in visited: 
                    continue
                visited.add(n)
                d = divide(n, y, visited)
                if d > 0: return d * g[x][n]
            return -1.0
        # use defaultdict can insert value into dictionary without existance
        g = collections.defaultdict(dict)
        for (x, y), v in zip(equations, values):      
            g[x][y] = v
            g[y][x] = 1.0 / v

        ans = [divide(x, y, set()) if x in g and y in g else -1 for x, y in queries]
        return ans
