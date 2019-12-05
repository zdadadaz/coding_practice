class Solution:
    # Note:
    # if size A is repeated to the size bigger than B, then we 
    # can say B is not in A even A grows to infinite size.    
    def repeatedStringMatch(self, A: str, B: str):
        lnA,lnB = len(A),len(B)
        # 3 because of 2 for rounding, 1 for range,
        times = int(lnB/lnA) + 3
        for i in range(1,times):
            # do not need to code strstr() function
            if B in A*i:
                return i
        return -1

