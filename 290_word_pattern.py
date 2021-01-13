class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        charmap = {}
        wordmap = {}
        str = str.split(' ')
        if len(pattern) != len(str):
            return False
        for i in range(len(str)):
            c = pattern[i]
            word = str[i]
            if (c in charmap) != (word in wordmap):
                return False
            if c in charmap:
                if charmap[c] != word or wordmap[word]!= c:
                    return False
            else:
                charmap[c] = word
                wordmap[word] = c
        return True
            