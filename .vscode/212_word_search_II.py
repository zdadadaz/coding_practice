class Tries:
    def __init__(self):
        self.endWord = False
        self.children = [None]*26
    def insert(self, word):
        cur = self
        for c in word:
            idx = ord(c) - ord('a')
            if cur.children[idx] == None:
                cur.children[idx] = Tries()
            cur = cur.children[idx]
        cur.endWord = True
    
class Solution:
    def dfs(self,i,j, trie,s):
        c = self.board[i][j]
        if c == '$': return
        self.board[i][j] = '$' # visited
        t = trie.children[ord(c)-ord('a')]
        if t != None:
            ss = s+c
            if t.endWord: self.result.add(ss)
            if i < len(self.board)-1: self.dfs(i+1, j, t,ss)
            if j < len(self.board[0])-1: self.dfs(i,j+1,t,ss)
            if i > 0: self.dfs(i-1,j,t,ss)
            if j > 0: self.dfs(i,j-1,t,ss)
        self.board[i][j] = c
        
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        if len(words)==0:
            return []
        trie = Tries() # root
        for w in words:
            trie.insert(w)
        
        self.result = set()
        self.board = board
        self.words = words
        for i in range(len(board)):
            for j in range(len(board[i])):
                self.dfs(i,j,trie,"")
        return list(self.result)
                