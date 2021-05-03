class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        n = len(heights)
        import heapq
        m = []
        b = 0
        res = 0 
        for i in range(1,n):
            diff = max(0, heights[i]-heights[i-1])
            if diff > 0:
                if len(m) < ladders:
                    heapq.heappush(m,diff)
                elif ladders !=0:
                    if diff > m[0]:
                        b += heapq.heappop(m)
                        heapq.heappush(m,diff)
                    else:
                        b += diff
                else: # ladders == 0 and len(m)>= ladders
                    b += diff
                if b > bricks:
                    break
            res+= 1
        return res

