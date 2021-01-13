class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        r = len(height)-1
        lwall = rwall = 0
        water = 0
        while l < r:
            if height[l] < height[r]:
                if height[l] < lwall:
                    water += lwall-height[l]
                else:
                    lwall = height[l]
                l+=1
            else:
                if height[r] < rwall:
                    water += rwall-height[r]
                else:
                    rwall = height[r]
                r-=1
        return water
                