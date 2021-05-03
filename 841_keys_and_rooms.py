class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n = len(rooms)
        que = [0]
        vis = set([0])
        while len(que)!=0:
            cur = que.pop()
            vis.add(cur)
            for k in rooms[cur]:
                if k not in vis:
                    que.append(k)
        return True if len(vis)==n else False