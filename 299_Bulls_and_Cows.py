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

# A = "1122"
# B = "2211"
A="1123"
B="0111"
sol = Solution()
print(sol.getHint(A,B))