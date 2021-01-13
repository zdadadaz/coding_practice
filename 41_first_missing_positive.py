class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        containOne = False
        for i in range(n):
            if nums[i] == 1:
                containOne = True
                break
        if not containOne:
            return 1

        for i in range(n):
            if nums[i]>n or nums[i]<1:
                nums[i] = 1
                # print(nums)
        for i in range(n):
            x = abs(nums[i])
            if nums[x-1] > 0:
                nums[x-1] = -nums[x-1]
        for i in range(n):
            if nums[i]>0:
                return i+1
        return n+1