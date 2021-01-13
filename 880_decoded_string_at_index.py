class Solution:
    def decodeAtIndex(self, S: str, K: int) -> str:
        size= 0
        for i in S:
            if i.isdigit():
                size*=int(i)
            else:
                size+=1
        
        for i in range(len(S)-1,-1,-1):
            K %= size
            if S[i].isalpha() and K == 0:
                return S[i]
            if S[i].isdigit():
                size /= int(S[i])
            else:
                size -= 1
        return -1