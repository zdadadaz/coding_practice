from collections import Counter
class Solution:
    def threeSumMulti(self, arr , target ) :
        module = 10**9 + 7
        m = Counter(arr)
        maxM = max(list(m.keys()))
        res = 0
        for i in range(target+1):
            for j in range(i,target+1):
                k = target - i - j
                if k < 0 or k>maxM or k < j:
                    continue
                if k not in m or i not in m or j not in m:
                    continue
                if (i==j==k):
                    res += m[i]*(m[i]-1)*(m[i]-2)/6 # if m[i]<3, m[i]-1 or m[i]-2 will be zero
                elif (i==j and j!=k):
                    res += m[i]*(m[i]-1)*m[k]/2
                elif (i!=j and j==k):
                    res += m[j]*(m[j]-1)*m[i]/2
                else:
                    res += m[i]*m[j]*m[k]
        return int(res%module)

# a = [1,1,2,2,3,3,4,4,5,5]
a = [1,2,3,4,5,6]
s = Solution()
print(s.threeSumMulti(a,3))