class Solution():
    def min_num_coin(self,clist,amnt,minCoin,coinsUsed):
        for i in range(0,amnt+1):
            coinNum = i
            newCoin = 1
            # successor
            for j in [l for l in clist if l <= i]:
                if minCoin[i-j]+1 < coinNum :
                    coinNum = minCoin[i-j]+1
                    newCoin = j
                # coinNum = min(coinNum,minCoin[i-j]+1)
            minCoin[i] = coinNum
            coinsUsed[i] = newCoin
        return minCoin[amnt]

    def print_coin(self,clist,amnt,coinsUsed):
        cur = amnt 
        out = []
        while cur >0:
            out.append(coinsUsed[cur])
            cur -= coinsUsed[cur]
        return out


amnt = 63
clist = [1,5,10,21,25]
minCoin = [0]*(63+1)
coinsUsed = [0]*(63+1)
sol = Solution()
print(sol.min_num_coin(clist, amnt,minCoin,coinsUsed))
print(sol.print_coin(clist,amnt,coinsUsed))