class Solution:
    # O(R*log(C))
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        r,c = len(matrix), len(matrix[0])
        def bst(arr): # [1,4]
            l, r = 0, len(arr)
            while l < r:
                mid = (l+r)//2
                if arr[mid] == target:
                    return mid
                elif arr[mid] < target:
                    l = mid+1
                else:
                    r = mid-1
            l = min(len(arr)-1, l)
            return l
        
        for i in range(r):
            idx = bst(matrix[i])
            if matrix[i][idx] == target:
                return True
        return False
    
    # O(M+N)
    def searchMatrix_fromtopright(self, matrix: List[List[int]], target: int) -> bool:
        r,c = len(matrix), len(matrix[0])
        rt = 0
        ct = c-1
        while rt<r and ct>-1:
            if matrix[rt][ct] == target:
                return True
            elif matrix[rt][ct] > target:
                ct -= 1
            elif matrix[rt][ct] < target:
                rt += 1
        return False