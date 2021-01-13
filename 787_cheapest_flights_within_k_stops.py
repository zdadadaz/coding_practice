import heapq
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        if len(flights)==0:
            return -1
        visited = {}
        heap = [(0,0,src)] # price, stops, node
        arr = []
        while len(heap) !=0:
            cur = heapq.heappop(heap)
            visited[cur[2]] = (cur[0], cur[1])
            if cur[2] == dst:
                return cur[0]
            if cur[1] <=K:
                for (node,newPrice,newStops) in self.gen_actions(cur, flights, K):
                    if node not in visited:
                        heapq.heappush(heap, (newPrice,newStops,node))
                        # need update price and stops, because using heap makes lower price node searched first
                        # but when lower price path over K+1, lower stops path need to update it.
                    elif newPrice<visited[node][0] or newStops<visited[node][1]:
                        heapq.heappush(heap, (newPrice,newStops,node))
                        visited[node] = (newPrice,newStops)
        return -1
    def gen_actions(self,cur,flights, K):
        for a in flights:
            if cur[2] == a[0] and cur[1]+1<=K+1:
                yield (a[1],cur[0]+a[2],cur[1] +1) # output connectedNode, price, stops
                
        