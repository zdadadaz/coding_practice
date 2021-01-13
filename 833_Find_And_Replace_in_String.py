class Solution:
    def findReplaceString(self, S: str, indexes: List[int], sources: List[str], targets: List[str]) -> str:
        out = S
        for (idx, s, t) in sorted(zip(indexes, sources, targets), reverse = True):
            len_s = len(s)
            if S[idx:(idx+len_s)] == s:
                out = out[0:idx] + t + out[(idx+len_s):] 
        return out
                