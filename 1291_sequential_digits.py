class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        nl = len(str(low))
        nh = len(str(high))
        digits = '0123456789'
        outs = []
        for n in range(nl,nh+1):
            for d in range(1, 10):
                if d + n <= 10:
                    out = int(digits[d:(d+n)])
                    if out>=low and out <= high:
                        outs.append(out)
        return outs