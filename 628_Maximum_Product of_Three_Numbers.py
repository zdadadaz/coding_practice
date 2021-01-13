class Solution:
    # O(NlogN)
    def maximumProduct(self, nums):
        if len(nums) < 3:
            return -1
        nums.sort()
        return max(nums[-1]*nums[-2]*nums[-3],nums[0]*nums[1]*nums[-1])
    # O(N)
    def maximumProduct_N(self, nums):
        if len(nums) < 3:
            return -1
        maxNum1 = float("-inf")
        maxNum2 = float("-inf")
        maxNum3 = float("-inf")

        minNum1 = float("inf")
        minNum2 = float("inf")
        for i in ((nums)):
            if i > maxNum1:
                maxNum3,maxNum2,maxNum1 = maxNum2,maxNum1,i
            elif i > maxNum2:
                maxNum3,maxNum2 = maxNum2,i
            elif i > maxNum3:
                maxNum3 = i
            
            if i < minNum1:
                minNum2, minNum1 = minNum1,i
            elif i < minNum2:
                minNum2 = i
        return max(maxNum1*maxNum2*maxNum3, minNum1*minNum2*maxNum1)

Sol = Solution()
print(Sol.maximumProduct_N([1,2,3]))