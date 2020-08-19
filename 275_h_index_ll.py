class Solution:
    def hIndex(self, citations):
        n = len(citations)
        l= 0
        r= n-1
        while l<=r:
            mid = (l+r)//2
            print(l,mid,r,citations[mid] < n-mid)
            if citations[mid] < n-mid:
                l = mid+1
            else:
                r = mid-1
        return n-l
        
    def hIndex_linear(self, citations):
        n = len(citations) 
        i = n-1
        while i >=0:
            print(i,citations[i],n-1,citations[i]<n-i)
            if citations[i]<=n-i:
                break
            i -=1
        return n-i

sol = Solution()
# print(sol.hIndex([0,1,3,4,5,6,10,13]))
print(sol.hIndex_linear([0,1,3,5,6]))

