class Monoque:
    def __init__(self):
        self.arr = []
        
    def push(self, e):
        while self.arr and e > self.arr[-1]:
            self.arr.pop(-1)
        self.arr.append(e)
    
    def pop(self):
        return self.arr[0]
    
    def erase(self, e):
        try:
            self.arr.remove(e)
        except:
            pass
        
    def len(self):
        return len(self.arr)
    
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        que = Monoque()
        res = []
        for i in range(len(nums)):
            que.push(nums[i])
            # print(que.arr)
            if i-k+1 >= 0:
                res.append(que.pop())
                if que.pop()==nums[i-k+1]:
                    que.erase(nums[i-k+1])
        return res
                