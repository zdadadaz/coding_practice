class Solution:
    def isValid(self, s: str) -> bool:
        bracket_l ={'{':0,'[':1,'(':2} 
        bracket_r ={'}':0,']':1,')':2} 
        # improvement
        # mapping = {")": "(", "}": "{", "]": "["}
        m = []
        for i in s:
            if i in bracket_l:
                m.append(i)
            else:
                if len(m)==0 or bracket_l[m[-1]] != bracket_r[i]:
                    return False
                m.pop()
        return True if len(m) ==0 else False

    def isValid_combine2map(self, s: str) -> bool:
        mapping = {")": "(", "}": "{", "]": "["}
        m = []
        for i in s:
            if i not in mapping:
                m.append(i)
            else:
                if len(m)==0 or mapping[i] != m[-1]:
                    return False
                m.pop()
        return True if len(m) ==0 else False