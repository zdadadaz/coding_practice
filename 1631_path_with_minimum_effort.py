class Solution:
    # DP TLE: O(max(w,h)*w*h) = O()
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        w,h = len(heights[0]),len(heights)
        m = [[float('inf')]*w for i in range(h)]
        m[0][0] = 0
        dirs = [0,-1,0,1,0]
        for k in range(max(w,h)):
            stable =True
            for i in range(h):
                for j in range(w):
                    for d in range(4):
                        tx = j + dirs[d]
                        ty = i + dirs[d+1]
                        if 0<=tx < w and 0<= ty< h: 
                            t = max(m[ty][tx], abs(heights[i][j]-heights[ty][tx]))
                            if t < m[i][j]:
                                m[i][j] = t
                                stable =False
            if stable:
                break
        return m[h-1][w-1]

    # TLE BST(cost)->BFS, O(mn*log(max(h) – min(h)))  O(mn)
    def minimumEffortPath_BST_BFS(self, heights: List[List[int]]) -> int:
        w,h = len(heights[0]),len(heights)
        def bfs(m):
            que = [(0,0)]
            dirs =[0,-1, 0, 1, 0]
            vis = set()
            while len(que)!=0:
                cur = que.pop(0)
                vis.add(cur)
                if cur == (h-1,w-1):
                    return True
                for d in range(4):
                    tx = cur[1]+dirs[d]
                    ty = cur[0]+dirs[d+1]
                    if 0<=tx<w and 0<=ty<h and (ty,tx) not in vis and abs(heights[ty][tx]-heights[cur[0]][cur[1]]) <=m:
                        que.append((ty,tx))
            return False
        maxv = 0
        minv = float('inf')
        for i in range(w):
            for j in range(h):
                maxv = max(maxv, heights[j][i])
                minv = min(minv, heights[j][i])
        l = 0
        r = maxv-minv
        while (l<r):
            mid = (l+r)//2
            if bfs(mid):
                r = mid
            else:
                l = mid+1
        return l
    # O(mnlog(mn))->O(Vlog(E)),O(mn)
    def minimumEffortPath_dijk(self, heights: List[List[int]]) -> int:
        import heapq
        w,h = len(heights[0]),len(heights)
        dist = [[float('inf')]*w for i in range(h)]
        dist[0][0]=0
        que = [(0,(0,0))]
        dirs =[0,-1, 0, 1, 0]
        while len(que)!=0:
            val, cur = heapq.heappop(que)
            if cur == (h-1,w-1):
                return val
            for d in range(4):
                tx = cur[1]+dirs[d]
                ty = cur[0]+dirs[d+1]
                if 0<=tx<w and 0<=ty<h:
                    cost =  abs(heights[ty][tx]-heights[cur[0]][cur[1]])
                    if max(val,cost)>=dist[ty][tx]:
                        continue
                    dist[ty][tx] = max(val,cost)
                    heapq.heappush(que, (max(val,cost), (ty,tx)))
        return -1
        