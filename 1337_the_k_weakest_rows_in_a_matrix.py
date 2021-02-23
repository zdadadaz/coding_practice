class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        r, c = len(mat), len(mat[0])
        soldierm = [[i,0] for i in range(r)]
        for i in range(r):
            for j in range(c):
                if mat[i][j] == 1:
                    soldierm[i][1]+=1
                else:
                    break
        soldierm.sort(key=lambda a: (a[1], a[0]))        
        return [soldierm[i][0] for i in range(k)]

    def kWeakestRows_sum(self, mat: List[List[int]], k: int) -> List[int]:
        r, c = len(mat), len(mat[0])
        soldierm = []
        for i in range(r):
            soldierm.append((sum(mat[i]),i))
        soldierm.sort()
        return [soldierm[i][1] for i in range(k)]


        


        

