class prefixword:
    def __init__(self):
        self.node=None
        self.endofword = False
        self.letters=[None]*26
    def gen_list(self, word):
        curNode = self
        for w in range(len(word)-1,-1,-1):
            widx = ord(word[w])-ord('a')
            if curNode.letters[widx] == None:
                curNode.letters[widx] = prefixword()
            curNode = curNode.letters[widx]
        curNode.endofword = True

class StreamChecker:    
    def __init__(self, words: List[str]):
        self.node = prefixword()
        for word in words:
            self.node.gen_list(word)
        self.quelist = []
    def query(self, letter: str) -> bool:
        self.quelist.append(letter)
        curNode = self.node
        for i in range(len(self.quelist)-1,-1,-1):
            idx = ord(self.quelist[i])-ord('a')
            if curNode.letters[idx] == None:
                return False
            curNode = curNode.letters[idx]
            if curNode.endofword ==True:
                return True
        return False

# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)