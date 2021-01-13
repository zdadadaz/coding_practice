class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # [-1,0,3,5,9,12], target = 9
        if len(nums)==0:
            return -1
        lt = 0
        rt = len(nums)-1
        while lt <= rt:
            mid = (lt+rt)//2
            if nums[mid] == target:
                return mid
            elif target < nums[mid]:
                rt = mid-1
            else:
                lt = mid+1
        return -1