class Solution():
    def edit_distance(self,A,B):
        sA,sB = len(A), len(B)
        mat = [[i for i in range(sA+1)] for j in range(sB+1)]
        for i in range(sA+1):
            for j in range(sB +1):
                if i ==0 or j ==0:
                    mat[j][i] = max(i,j)
                else:
                    if A[i-1] == B[j-1]:
                        mat[j][i] = mat[j-1][i-1]
                    else:
                        tmp = min(mat[j-1][i-1]+1,mat[j-1][i]+1)
                        mat[j][i] = min(tmp,mat[j][i-1]+1)
        return mat[-1][-1]

A = 'university'
B = 'unavafsity'
sol = Solution()
print(sol.edit_distance(A,B))