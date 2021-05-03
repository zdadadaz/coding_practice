class Solution:
    def minimumLengthEncoding_set(self, words: List[str]) -> int:
        n = len(words)
        W = set(words)
        for w in words:
            wn = len(w)
            for i in range(1,wn):
                if w[-i:] in W:
                    W.remove(w[-i:])
        return len('#'.join([i for i in W]))+1

    # sufix tree
    def minimumLengthEncoding_suftree(self, words: List[str]) -> int:
        n = len(words)
        words = list(set(words))
        t = Trie()
        for w in words:
            t.insert(w[::-1])
        return sum([wlen for letter, wlen in t.res if len(letter) == 0])

class Trie:
    def __init__(self):
        self.letters = {}
        self.res = [] # (letters, word len)
        
    def insert(self, word):
        cur = self
        for w in word:
            if w not in cur.letters:
                cur.letters[w] = Trie()
            cur = cur.letters[w]
        self.res.append((cur.letters, len(word)+1))

    