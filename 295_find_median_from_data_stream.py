class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        from heapq import heappush,heappop
        self.minheap = [float('inf')]
        self.maxheap = [float('inf')]
        
    def addNum(self, num: int) -> None:
        if num > self.maxheap[0] or ( -self.minheap[0] <= num <= self.maxheap[0] and len(self.minheap)==len(self.maxheap)):
            heappush(self.maxheap, num)
        else:
            heappush(self.minheap, -num)
            
        if len(self.minheap)-len(self.maxheap)>1:
            heappush(self.maxheap, -heappop(self.minheap))
        elif len(self.maxheap)-len(self.minheap)>1:
            heappush(self.minheap, -heappop(self.maxheap))
        
    def findMedian(self) -> float:
        if len(self.minheap)==len(self.maxheap):
            return (-self.minheap[0]+self.maxheap[0])/2;
        else:
            if len(self.minheap) > len(self.maxheap):
                return -self.minheap[0]
            else:
                return self.maxheap[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()