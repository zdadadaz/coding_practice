class Node():
    def __init__(self, var):
        self.id = var 
        self.connectTo = {}

    def add_connect(self, var, val):
        self.connectTo[var] = val
    
    def get_connect(self):
        return self.connectTo.keys()

    def __eq__(self, other):
        if self.id == other:
            return True
        else:
            return False

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        nodes = {}
        for i in range(len(values)):
            self.add_node(equations[i][0], equations[i][1],values[i], nodes)

        out =[]
        for q in queries:
            out.append(self.dfs(nodes, q[0], q[1]))

        return out

    def dfs(self, nodes, start, goal):
        if start not in nodes or goal not in nodes:
            return -1.0
        if start == goal:
            return 1.0
        
        visited = set()
        queue = [(start,-1)]
        
        while len(queue) > 0:
            cur, res = queue.pop(0)
            visited.add(cur)
            if cur == goal:
                return res
            for conn in nodes[cur].get_connect():
                if conn in visited:
                    continue
                if res == -1:
                    tmp = nodes[cur].connectTo[conn] 
                else:
                    tmp = res * nodes[cur].connectTo[conn]
                queue.append((conn, tmp))
        return -1.0
        
    
    def add_node(self, varA, varB, value, nodes):
        if varA not in nodes:
            node = Node(varA)
            node.add_connect(varB, value)
            node.add_connect(varA, 1.0)
            nodes[varA]=node
        else:
            nodes[varA].add_connect(varB, value)
            
        if varB not in nodes:
            node = Node(varB)
            node.add_connect(varA, 1.0/float(value))
            node.add_connect(varB, 1.0)
            nodes[varB]=node
        else:
            nodes[varB].add_connect(varA, 1.0/float(value))
            
            
    
    
