class Solution:
    def minJumps(self, arr: List[int]) -> int:
        n = len(arr)
        que = [0]
        vis = set([0])
        cnt = 0
        from collections import defaultdict
        pos = defaultdict(list)
        for i, num in enumerate(arr):
            pos[num].append(i)
        while len(que) !=0:
            for _ in range(len(que)):
                cur = que.pop(0)
                if cur == n-1:
                    return cnt
                nexts = [cur-1, cur+1] + pos[arr[cur]]
                for nx in nexts:
                    if 0<=nx<n and nx not in vis:
                        vis.add(nx)
                        que.append(nx)
                pos[arr[cur]] = []
            cnt+=1
        return -1