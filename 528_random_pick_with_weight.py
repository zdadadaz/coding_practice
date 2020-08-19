import random 
class Solution:

    def __init__(self, w):
    
        self.presum = [0]*len(w)
        self.presum[0] = w[0]
        for i in range(1,len(w)):
            self.presum[i] = self.presum[i-1] + w[i]

    def pickIndex(self,rand_value):
        rand_value = random.randint(0,self.presum[-1]-1)
        lt = 0
        rt = len(self.presum)-1
        # terminate condition: ex [0 1] or [1 2] or [2 3]  
        while  lt+1 < rt:
            mid = (lt+rt)//2
            if rand_value < self.presum[mid]:
                rt = mid
            else:
                lt = mid
        # compare with lt: because [0 1 2] -> lt [0] ->rt [1 2]
        if rand_value < self.presum[lt]:
            return lt
        return rt

    #test case:
    # 0,1,2,3 
    # mid =1, <, mid =0 , >, 
sol = Solution([1,2,3,4])
print([sol.pickIndex(i) for i in range(10)])

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()