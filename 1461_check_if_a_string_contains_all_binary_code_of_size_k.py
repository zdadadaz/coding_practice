class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        n = len(s)
        vis = set()
        for i in range(n-k+1):
            vis.add(s[i:(i+k)])
            if len(vis) == (2**k):
                return True
        return False

    def hasAllCodes_rolling_hash(self, s: str, k: int) -> bool:
        n = len(s)
        m = 1<<k
        got = [False]* m
        hash_val = 0
        allone = m - 1
        for i in range(n):
            hash_val = ((hash_val<<1) & allone) | (int(s[i]))
            if i >= k-1 and got[hash_val] == False:
                got[hash_val] = True
                m -=1
                if m== 0 :
                    return True
        return False