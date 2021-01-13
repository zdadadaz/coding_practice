import collections
class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        dicts = {}
        dicts = collections.defaultdict(int)
        A = 0
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                A+=1
            else:
                dicts[secret[i]] += 1
        B = 0
        for i in range(len(guess)):
            if secret[i] != guess[i] and dicts[guess[i]] >0:
                B += 1
                dicts[guess[i]] -= 1
        out = ""
        out += str(A)+"A"
        out += str(B)+"B"
        return out

class Solution2:
    def getHint(self, secret: str, guess: str) -> str:
        A = 0
        buck =[0]*10
        n = len(secret)
        for i in range(n):
            buck[int(secret[i])]+=1
            buck[int(guess[i])]-=1
            if secret[i] == guess[i]:
                A+=1
        acc = 0
        for i in range(10):
            if buck[i]>0:
                acc+=buck[i]
        B = n - A - acc
        return str(A)+'A'+str(B)+'B'
                
                
# A = "1122"
# B = "2211"
A="1123"
B="0111"
sol = Solution()
print(sol.getHint(A,B))