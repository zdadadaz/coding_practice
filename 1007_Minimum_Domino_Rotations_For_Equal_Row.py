class Solution:
    def minDominoRotations(self, A: List[int], B: List[int]) -> int:
        if len(A) <=1:
            return 0
        def helper(target, A, B):
            count = 0
            for index in range(len(A)):
                a,b = A[index], B[index]
                if target ==a:
                    continue
                else:
                    if target == b:
                        count +=1
                    else:
                        count = float('inf')
                        break
            return count
        
        out = min(min( helper(i, A, B) for i in [A[0],B[0]]),
            min( helper(i, B, A) for i in [A[0],B[0]]))
        return -1 if out ==float('inf') else out