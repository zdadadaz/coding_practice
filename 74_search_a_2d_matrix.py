class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if len(matrix)==0:
            return False
        idx = self.binary_search_V(matrix, target)
        out = self.binary_search_H(matrix, target, idx)
        return out
        
    def binary_search_V(self, matrix, target):
        c = len(matrix[0])
        lt = 0
        rt = len(matrix)-1
        while lt < rt:
            mid = (lt+rt)//2
            if target < matrix[mid][0]:
                rt = mid-1
            elif target > matrix[mid][c-1]:
                lt = mid+1
            else:
                lt = mid
                break
        return lt
    
    def binary_search_H(self, matrix, target, idx):
        lt = 0
        rt = len(matrix[0])-1
        while lt <= rt:
            mid = (lt+rt)//2
            if target < matrix[idx][mid]:
                rt = mid-1
            elif target > matrix[idx][mid]:
                lt = mid+1
            else:
                lt = mid
                return True
        return False
        