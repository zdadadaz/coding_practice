class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        cnt0 = 0
        cnt1 = 0
        cur = 1
        if s[0] == '0':
            cur = 0
        res = 0
        for i in s:
            if i=='0':
                if cur == 0:
                    cnt0 += 1
                else:
                    cur = 0
                    cnt0 = 1
                # print(cnt0, cnt1, res)
                res += 1 if cnt0<=cnt1 else 0
            else :
                if cur == 1:
                    cnt1 += 1
                else:
                    cur = 1
                    cnt1 = 1
                # print(cnt0, cnt1, res)
                res += 1 if cnt1<= cnt0 else 0
        return res

    def countBinarySubstrings_lean_code(self, s: str) -> int:
        cur=1
        prv=ans = 0
        for i in range(1,len(s)):
            if s[i]!= s[i-1]:
                ans += min(cur, prv)
                prv = cur
                cur = 1
            else:
                cur += 1
        return ans + min(cur, prv)