class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        m = len(s)
        T = [[False for j in range(m)] for i in range(m)]
        for wlen in range(1, m+1):
            for start in range(0, m-wlen+1):
                end = start + wlen - 1
                str_tmp = s[start:end+1]
                if str_tmp in wordDict:
                    T[start][end] = True
                    continue
                
                for split in range(start+1, end+1):
                    if (T[start][split-1] != False and T[split][end] != False):
                        T[start][end] = True
                        break
        return T[0][m-1]

