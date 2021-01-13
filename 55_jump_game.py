class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_reach = 0
        for i in range(len(nums)-1):
            if nums[i]+i >max_reach:
                max_reach = nums[i]+i
            if max_reach == i:
                break
        if max_reach>= len(nums)-1:
            return True
        return False

# TLE
# class Solution:
#     def canJump(self, nums: List[int]) -> bool:
#         def dfs(i):
#             if i == len(nums)-1:
#                 return True
#             if i >= len(nums):
#                 return False
#             if nums[i]==0:
#                 return False
#             for j in range(1,nums[i]+1):
#                 if dfs(i+j):
#                     return True
#             return False
#         return dfs(0)
        