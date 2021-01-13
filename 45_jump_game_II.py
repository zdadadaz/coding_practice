class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums)==1 or nums[0]==0:
            return 0
        far = nums[0]
        cur = nums[0]
        jump = 1
        for i in range(1, len(nums)):
            if i == len(nums)-1:
                return jump
            far = max(far, nums[i] + i)
            if i == cur:
                cur= far
                jump+=1
        return jump

# # TLE
# class Solution:
#     def jump(self, nums: List[int]) -> int:
#         arr = [0]*len(nums)
#         for i in range(len(nums)):
#             for j in range(min(1,nums[i]),nums[i]+1):
#                 moveidx = min(i+j, len(nums)-1)
#                 if moveidx == i:
#                     break
#                 else:
#                     if arr[moveidx] != 0:
#                         arr[moveidx] = min(arr[moveidx], arr[i]+1)
#                     else:
#                         arr[moveidx] = arr[i]+1
#         if arr[-1] != 0:
#             return arr[-1]
#         return 0