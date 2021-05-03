class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []
        res = [[1]]
        i = 1
        while i <numRows:
            tmp = [1]
            prv = res[-1]
            for j in range(0,len(prv)-1):
                tmp.append(prv[j+1]+prv[j])
            tmp.append(1)
            res.append(tmp)
            i += 1
        return res