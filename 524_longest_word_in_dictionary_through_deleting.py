class Solution:
    def findLongestWord(self, s: str, d: List[str]) -> str:
        res = 0
        lens = len(s)
        out = ""
        for w in d:
            lenw = len(w)
            if lenw>lens:
                continue
            wl = sl = 0
            while sl < lens and wl < lenw:
                if s[sl] == w[wl]:
                    sl += 1
                    wl += 1
                else:
                    sl += 1
            if wl ==lenw:
                if res < lenw:
                    res = max(res, lenw)
                    out = w
                elif res == lenw:
                    if out > w:
                        out = w
        return out