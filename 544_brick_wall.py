class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        from collections import defaultdict
        
        def accsum(arr):
            for i in range(1,len(arr)):
                arr[i] += arr[i-1]
                self.maxvalue = max(self.maxvalue, arr[i])
            return arr
        n = len(wall)
        self.maxvalue = wall[0][0]
        m = Counter(accsum(wall[0]))
        for r in range(1,n):
            m += Counter(accsum(wall[r]))
        res = n
        for i in m.keys():
            if i != self.maxvalue: 
                res = min(n-m[i], res)
        return res

    def leastBricks_combine_counter_and_acc(self, wall: List[List[int]]) -> int:
        from collections import defaultdict
        m = defaultdict(int)
        n = len(wall)
        for r in wall:
            prv = 0
            for b in r[:-1]:
                prv += b
                m[prv] +=1
        # for [[1],[1],[1]]
        if not m:
            return n
        return n - max(m.values())