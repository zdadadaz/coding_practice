class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        cand1 =None
        cand2 =None
        count1 = 0
        count2 = 0
        for n in nums:
            if cand1 == n:
                count1+=1
            elif cand2 == n:
                count2+=1
            elif count1 ==0:
                cand1 = n
                count1 +=1
            elif count2 == 0:
                cand2 = n
                count2 +=1
            else:
                count1,count2 = count1-1, count2-1
        
        return [x for x in [cand1, cand2] if nums.count(x) > len(nums)//3]