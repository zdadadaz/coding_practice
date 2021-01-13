class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        l = []
        for npp, start, end in trips:
            l.append((start,npp))
            l.append((end,-npp))
        l.sort()
        for _,n in l:
            capacity -= n
            if capacity<0:
                return False
        return True