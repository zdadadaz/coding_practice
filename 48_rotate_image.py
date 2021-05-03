class Solution:
    def rotate_traverse_flip(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n,m = len(matrix),len(matrix[0])
        for i in range(n):
            for j in range(m):
                if i == j or i > j:
                    continue
                matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]
        for i in range(n):
            for j in range(m//2):
                matrix[i][j],matrix[i][m-j-1] = matrix[i][m-j-1],matrix[i][j]
                

    def rotate_intuition(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n,m = len(matrix),len(matrix[0])
        
        for i in range(n//2+n%2):
            for j in range(n//2):
                tmp = matrix[n-1-j][i]
                matrix[n-1-j][i] = matrix[n-1-i][n-1-j]
                matrix[n-1-i][n-1-j] = matrix[j][n-1-i]
                matrix[j][n-1-i] = matrix[i][j]
                matrix[i][j] = tmp