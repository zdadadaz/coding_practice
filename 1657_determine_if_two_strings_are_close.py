class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        n1 = len(word1)
        n2 = len(word2)
        if n1 != n2:
            return False
        
        c1 = Counter(word1)
        c2 = Counter(word2)
        n1 = Counter([i for i in c1.values()]) ## freq 
        n2 = Counter([i for i in c2.values()])

        return c1==c2 or (n1 ==n2 and set(word1) == set(word2))