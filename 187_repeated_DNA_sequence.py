class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        d = {}
        for i in range(len(s)-9):
            if s[i:(i+10)] not in d:
                d[s[i:(i+10)]] = 0
            d[s[i:(i+10)]] += 1
        return [key for key, value in d.items() if value>1]