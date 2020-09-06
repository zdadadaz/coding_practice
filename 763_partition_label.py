class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        arr = [0]*26
        for idx,i in enumerate(S):
            arr[ord(i)-ord('a')] = idx
        start = 0
        end = 0
        res = []
        for idx,i in enumerate(S):
            end = max(end, arr[ord(i)-ord('a')])
            if idx == end:
                res.append(end-start+1)
                start = end+1
        return res