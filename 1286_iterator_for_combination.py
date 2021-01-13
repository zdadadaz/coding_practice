class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        self.char = characters
        self.clen = combinationLength
        self.vis = []
        # self._dfs(0,combinationLength,'')
        self._dfs('',characters)
        
    # def _dfs(self,start, length,txt):
    #     if length==0:
    #         self.vis.append(txt)
    #         return 
    #     for i in range(start, len(self.char)-length + 1):
    #         self._dfs(i+1,length-1,txt+self.char[i])
        
    def _dfs(self, que, char):
        if len(que) == self.clen: #Big hole!!! -> and que not in self.vis:
            self.vis.append(que)
            return 
        for idx in range(0,len(char)):
            self._dfs(que+char[idx],char[idx+1:])
            
    def next(self) -> str:
        return self.vis.pop(0)

    def hasNext(self) -> bool:
        return len(self.vis)!=0


# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()