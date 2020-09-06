class Solution:

    def __init__(self, rects: List[List[int]]):
        self.numPt= 0
        self.acc = []
        self.rects = rects
        for idx,i in enumerate(rects):
            self.numPt += (i[2]-i[0]+1)*(i[3]-i[1]+1)
            self.acc.append(self.numPt)
            
    def pick(self) -> List[int]:
        import random
        idx = random.randint(0,self.numPt-1)
        l,r = 0, len(self.rects)-1
        while l<r:
            mid = (l+r)//2
            if self.acc[mid] <= idx: # ex8,20,30->8 in a[1]
                l = mid+1
            else:
                r = mid
        rect= self.rects[l]
        xpts = rect[2]-rect[0]+1
        ypts = rect[3]-rect[1]+1
        pts_rect = xpts*ypts
        pstart = self.acc[l]-pts_rect
        offset = idx-pstart
        return [rect[0]+offset % xpts, rect[1]+offset//xpts]
        
        

# Your Solution object will be instantiated and called as such:
# obj = Solution(rects)
# param_1 = obj.pick()