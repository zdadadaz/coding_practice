class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        def dfs(cur, vis):
            vis[cur] = False
            if arr[cur] == 0:
                return True
            left = cur - arr[cur] if cur >= arr[cur] else -1
            right = cur + arr[cur] if cur + arr[cur] < len(arr) else -1
            
            lt = rt = False
            if left != -1 and left not in vis:
                lt = dfs(left, vis)
            if right != -1 and right not in vis:
                rt = dfs(right, vis)
            vis[cur] = lt | rt
            return vis[cur]
        vis = {}
        return dfs(start, vis)