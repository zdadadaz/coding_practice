class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        if len(nums)==1:
            return str(nums[0])
        out = self.mergesort(nums) 
        if out[0]=='0':
            return '0'
        return ''.join(out)
    def mergesort(self, nums):
        if len(nums)==1:
            return nums
        l = 0
        r = len(nums)
        mid = (l+r)//2
        ll = self.mergesort(nums[l:mid])
        rr = self.mergesort(nums[mid:r])
        out = self.merge(ll, rr)
        return out
    def merge(self, ll,rr):
        out = []
        il = 0
        ir = 0
        while il < len(ll) and ir < len(rr):
            lnum = str(ll[il])
            rnum = str(rr[ir])
            tmpout = 0
            if int(lnum+rnum) > int(rnum+lnum):
                tmpout = lnum
                il+=1
            else:
                tmpout = rnum
                ir+=1
            out.append(tmpout)
        if il < len(ll):
            for q in range(il, len(ll)):
                out.append(str(ll[q]))
        if ir < len(rr):
            for q in range(ir, len(rr)):
                out.append(str(rr[q]))
        return out

                
                        
        