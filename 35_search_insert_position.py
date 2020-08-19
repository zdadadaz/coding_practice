class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        lt = 0
        rt = len(nums)-1
        while lt <= rt:
            mid = (lt+rt)//2
            if nums[mid]>target:
                rt = mid-1
            elif nums[mid]<target:
                lt = mid+1
            else:
                return mid
        return lt
    # testcase [1,3,5,6], 5
    # 2
    # lt=0,rt=3, mid=1, due to nums[1]==3 < 5 so lt = 2
    # lt=2,rt=3, mid=2, due to nums[2]==5 ==5 so return 
    
    # testcase [1,3,5,6], 2
    # 1
    # lt=0,rt=3,mid=1, due to nums[1]==3 > 2 so rt = 0
    # lt=0,rt=0,mid=0, due to nums[0]==1 < 2 so lt = 1
    # lt=1,rt=0, return lt
    
    # testcase [1,3,5,6], 7
    # 4
    # lt=0,rt=3,mid=1, due to nums[1]==3 < 7 so lt = 2
    # lt=2,rt=3,mid=2, due to nums[2]==5 < 7 so lt = 3
    # lt=3,rt=3,mid=3, due to nums[3]==6 < 7 so lt = 4
    # lt=4,rt=3, return lt
    
    # [1,3,5,6], 0
    # 0
    # lt=0,rt=3,mid=1, due to nums[1]==3 > 0 so rt = 0
    # lt=0,rt=0,mid=0, due to nums[0]==1 > 0 so rt = -1
    # lt=0,rt=-1, return lt
    def searchInsert_web(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n = len(nums)
        out=None
        for i in range(n):
            if nums[i]>=target:
                out = i
                break
        return n if out==None else out