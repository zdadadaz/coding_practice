class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        setn = set(nums)
        maxlen = 0
        for i in nums:
            if i-1 not in setn and i in setn and i+1 in setn:
                count = 1
                start = i
                while count < len(nums) and start+1 in setn:
                    start+=1
                    count+=1
                maxlen = max(count,maxlen)
        if maxlen==0 and len(setn)>0:
            return 1
        return maxlen