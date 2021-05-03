class Solution:
    def longestValidParentheses(self, s: str) -> int:
        m = [-1]
        res = 0
        for idx,i in enumerate(s):
            # append '('
            if i == '(':
                m.append(idx)
            else:
                m.pop()
                # append barrier
                if not m:
                    m.append(idx)
                else:
                    res = max(res,idx-m[-1])
        return res

    def longestValidParentheses_two_pointer(self, s: str) -> int:
        l = 0
        r = 0
        res_left = 0
        for i in s:
            res = 0
            if i == '(':
                l+=1
            else:
                r +=1
            if r==l:
                res_left = max(res_left, l+r)
            elif r>l:
                r=l=0
        
        l = 0
        r = 0
        res_right = 0
        for i in s[::-1]:
            res = 0
            if i == '(':
                l+=1
            else:
                r +=1
            if r==l:
                res_right = max(res_right, l+r)
            elif l>r:
                r=l=0
        return max(res_right, res_left)
                    