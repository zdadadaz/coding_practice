class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        # return ''.join(word1)== ''.join(word2)
        for w1, w2 in zip(self.gen(word1), self.gen(word2)):
            if w1 != w2:
                return False
        return True
        
    def gen(self, word):
        for w in word:
            for s in w:
                yield s
        yield None