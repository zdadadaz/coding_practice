class Solution:
    def wordSubsets_TLE(self, A: List[str], B: List[str]) -> List[str]:
        m = [Counter(a) for a in A]
        n = [Counter(b) for b in B]
            
        res = []
        for j in range(len(A)):
            flag = True
            for i in range(len(B)):
                b = n[i]
                for bb in b:
                    if bb not in m[j] or b[bb] > m[j][bb]:
                        flag = False
                        break
            if flag:
                res.append(A[j])
        return res

    def wordSubsets_linear(self, A: List[str], B: List[str]) -> List[str]:
        m = [Counter(a) for a in A]
        from collections import defaultdict
        n = defaultdict(int)
        for i in B:
            b = Counter(i)
            for j in b:
                if b[j] > n[j]:
                    n[j] = b[j]
            
        res = []
        for j in range(len(A)):
            flag = True
            for i in n:
                if i not in m[j] or n[i] > m[j][i]:
                    flag =False
                    break
            if flag:
                res.append(A[j])
                
        return res
    
    def wordSubsets_official(self, A, B):
        def count(word):
            ans = [0] * 26
            for letter in word:
                ans[ord(letter) - ord('a')] += 1
            return ans

        bmax = [0] * 26
        for b in B:
            for i, c in enumerate(count(b)):
                bmax[i] = max(bmax[i], c)

        ans = []
        for a in A:
            if all(x >= y for x, y in zip(count(a), bmax)):
                ans.append(a)
        return ans