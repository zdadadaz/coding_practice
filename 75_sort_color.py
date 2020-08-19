class Solution:
    def sortColors(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        self.recur(nums,0,len(nums)-1)
        
    def recur(self,nums, lt, rt):
        if lt<rt:
            print(lt,rt)
            pivot_idx = self.rearrange(nums, lt, rt)
            print(pivot_idx)
            self.recur(nums,lt,pivot_idx-1)
            self.recur(nums,pivot_idx+1,rt)
    
    def rearrange(self,nums, lt, rt):
        pivot = nums[rt]
        i = lt-1
        for j in range(lt,rt):
            if nums[j] < pivot:
                i+=1
                nums[i],nums[j] = nums[j],nums[i]
        i+=1
        nums[rt], nums[i] = nums[i], nums[rt]
        return i
    # two pointers
    def sortColors_web(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        lt = 0
        rt = len(nums)-1
        i=0
        while i<=rt:
            if nums[i]==0:
                nums[i],nums[lt] = nums[lt],nums[i]
                lt+=1
                i+=1
            elif nums[i]==2:
                nums[i],nums[rt] = nums[rt],nums[i]
                rt-=1
            else:
                i+=1
    
sol = Solution()
input= [2,0,2,1,1,0]
sol.sortColors(input)
print(input)
# Input: [2,0,2,1,1,0]
# Output: [0,0,1,1,2,2]
# lt=0,rt=5, pivot=2,lt=6,rt=1,out,swap pivot 5, [0,0,2,1,1,2] (n,n,n,n,n,y)
# lt=0,rt=4, pivot=0,lt=2,rt=-1,out,swap pivot 1, [0,0,2,1,1,2] (n,y,n,n,n,y)

        