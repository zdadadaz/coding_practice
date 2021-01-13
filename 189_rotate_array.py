class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def reverse(nums, l, r):
            while l < r:
                nums[l],nums[r] = nums[r],nums[l]
                l+=1
                r-=1
        k = k%len(nums)
        reverse(nums,0,len(nums)-1)
        reverse(nums,0,k-1)
        reverse(nums,k,len(nums)-1)
        


