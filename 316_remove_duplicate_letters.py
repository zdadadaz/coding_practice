class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        letters = { char: idx for idx, char in enumerate(s)}
        res = []
        for idx, char in enumerate(s):
            if char not in res:
                # char is at the front, char is smaller in lexical,
                while res and idx < letters[res[-1]] and char < res[-1]:
                    res.pop()
                res.append(char)
        return ''.join(res)
            