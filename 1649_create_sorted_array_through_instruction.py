class Solution:
    def createSortedArray(self, instructions: List[int]) -> int:
        from sortedcontainers import SortedList
        mod = 10**9 + 7
        s = SortedList()
        tot = 0
        for x in instructions:
            lt = s.bisect_left(x)
            rt = s.bisect_right(x)
            tot += min(lt, len(s)-rt)
            tot %=mod
            s.add(x)
        return tot %mod

    def createSortedArray_fenwick(self, instructions: List[int]) -> int:
        self.bit = [0]*100002
        mod = 10**9 + 7
        n = len(instructions)
        ans = 0
        for i in range(n):
            ans += min(self.sum(instructions[i]-1), i-self.sum(instructions[i]))
            ans %= mod
            self.update(instructions[i])
        return ans
    # O(logn) ->sum
    def sum(self, i): # get count 
        ans = 0
        j = i
        while j>0:
            ans += self.bit[j]
            j -= (j&-j)
        return ans
    
    def update(self, i): # update count
        j = i
        while j < 100002:
            self.bit[j] += 1
            j+= (j&-j)
    