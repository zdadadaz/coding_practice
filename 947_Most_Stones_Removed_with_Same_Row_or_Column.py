import collections
class Solution:
    def removeStones(self, stones):
        visited = set()
        removeable_stone_number = 0
        d = collections.defaultdict(list)
        for i,j in stones:
            d[i].append(j)
        dc = collections.defaultdict(list)
        for i,j in stones:
            dc[j].append(i)
        drc = {}
        drc['row'] = d
        drc['col'] = dc
        
        for s in stones:
            if str(s) not in visited:
                removeable_stone_number += (self.dfs(stones, visited, s, drc)-1)
        return removeable_stone_number
        
    def dfs(self, stones, visited, start, drc):
        queue, connected_number =[], 0
        queue.append(start)
        while len(queue)!= 0:
            cur = queue.pop()
            visited.add(str(cur))
            connected_number += 1
            self.successors(cur, stones, queue, visited, drc)
        return connected_number
        
    def successors(self, cur, stones, queue, visited, drc):
        for y in drc['row'][cur[0]]:
            if str([cur[0],y]) not in visited:
#                print([cur[0],y])
                queue.append([cur[0],y])
                visited.add(str([cur[0],y]))
        for x in drc['col'][cur[1]]:
            if str([x, cur[1]]) not in visited:
#                print([x, cur[1]])
                queue.append([x, cur[1]])
                visited.add(str([x, cur[1]]))

sol = Solution()
stones = [[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]
print(sol.removeStones(stones))