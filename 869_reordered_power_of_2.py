class Solution:
    def reorderedPowerOf2(self, N: int) -> bool:
        # 1,2,4,8,16,32,64,128,256,512,1024
        if N == 1:
            return True
        dm = {}
        m = set()
        for i in range(1,34):
            dm[i] = Counter(str(2**i))
        n_c= Counter(str(N))
        for d in dm:
            if n_c == dm[d]:
                return True
        return False

    def reorderedPowerOf2_counter(self, N: int) -> bool:
        # 1,2,4,8,16,32,64,128,256,512,1024
        if N == 1:
            return True
        
        n_c= Counter(str(N))
        for i in range(1,34):
            if n_c == Counter(str(2**i)):
                return True
        return False