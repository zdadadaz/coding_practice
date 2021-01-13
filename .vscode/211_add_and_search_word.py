class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.endWord = False
        self.children = [None]*26
        
    def insert(self, word):
        cur = self
        for c in word:
            idx = ord(c) - ord('a')
            if cur.children[idx] == None:
                cur.children[idx] = WordDictionary()
            cur = cur.children[idx]
        cur.endWord = True
        
    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        self.insert(word)

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        cur = self
        for ix,i in enumerate(word):
            idx = ord(i) - ord('a')
            print(i,idx,word)
            if i == '.':
                for a in cur.children:
                    if a is not None and a.search(word[ix+1:]):
                        return True
                return False
            if cur.children[idx] == None:
                return False
            cur = cur.children[idx]
            
        return cur != None and cur.endWord
        


# Your WordDictionary object will be instantiated and called as such:

obj = WordDictionary()
for word in ["bad","dad","mad"]:
    obj.addWord(word)
for word in [".ad"]:
    param_2 = obj.search(word)
    print(param_2)