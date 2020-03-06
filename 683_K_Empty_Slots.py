class Solution:
    """
    @param flowers: the place where the flower will open in that day
    @param k:  an integer
    @return: in which day meet the requirements
    """
    def kEmptySlots(self, flowers, k):
        # Write your code here
        N = len(flowers)
        days= [0]*N
        for i in range(N):
            days[flowers[i]-1] = i+1
        
        res = float('inf')
        left = 0
        right = k + 1
        i = 0
        while right < N:
            i += 1
            if days[i] > days[left] and days[i] > days[right]:
                continue
            if i==right:
                res = min(res, max(days[right], days[left]))
            left = i
            right = i + k + 1
        res = res if res != float('inf') else -1
        return res