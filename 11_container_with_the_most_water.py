class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height)-1
        mV = 0
        while l < r:
            mV = max(mV, (r-l) * min(height[r],height[l]))
            if height[r] < height[l]:
                r-= 1
            else:
                l+=1
        return mV