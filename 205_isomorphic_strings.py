class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        m = {}
        mt = set()
        for i,w in enumerate(s):
            if w not in m:
                if t[i] in mt:
                    return False
                m[w] = t[i]
                mt.add(t[i])
            else:
                if m[w] != t[i]:
                    return False
        return True


    def isIsomorphic_values(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        m = {}
        for i,w in enumerate(s):
            if w not in m:
                if t[i] in m.values():
                    return False
                m[w] = t[i]
            else:
                if m[w] != t[i]:
                    return False
        return True