class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        from collections import defaultdict,deque
        
        graph = defaultdict(list)
        for i in tickets:
            graph[i[0]].append(i[1])
        for k in graph.keys():
            graph[k].sort(reverse=True)
        res=[]    
        self.dfs(graph,'JFK',res)
        return res[::-1]
        
    def dfs(self,graph,source,res):
        while graph[source]:
            v = graph[source].pop()
            self.dfs(graph,v,res)
        res.append(source)