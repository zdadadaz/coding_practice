class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        res = []
        while columnNumber > 0:
            cur = (columnNumber-1)%26
            columnNumber =  (columnNumber-1)//26 
            res.append(chr(cur+ord('A')))
        return ''.join(res[::-1])
            

 