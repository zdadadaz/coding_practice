# improvement: using heap
import copy
class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        N = len(costs)
        diff = [c[0] - c[1] for c in costs]
        indices =  sorted(range(0,N), key=lambda k:diff[k])
        result = 0
        for i in range(int(N/2)):
            result += costs[indices[i]][0]
            result += costs[indices[N-i-1]][1]
        return result