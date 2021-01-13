import copy
class Solution:
    def change(self, amount, coins):
        # dp = [0] * (amount + 1)
        # dp[0] = 1
        # for coin in coins:
        #     for i in range(1, amount + 1):
        #         if coin <= i:
        #             dp[i] += dp[i - coin]
        #     print(dp)
        # return dp[amount]

        # # recursive version
        state = [0]*len(coins)
        visited = []
        return self.recur(amount,state,coins,{},visited)
        # return len(visited)
        
    def recur(self,amount,state, coins,_V,visited):
        if amount == 0:
            if state not in visited:
                visited.append(state)
                # print(state)
                return (1,'sucuss')
            else:
                return (0,'repeat')
        else:
            if tuple(state) not in _V:
                acc = 0
                rec = []
                for idx,a in enumerate(coins):
                    if a <= amount:
                        state_tmp = copy.deepcopy(state)
                        state_tmp[idx] += 1
                        tmp =self.recur(amount-a,state_tmp,coins,_V,visited)[0]
                        rec.append([tmp, amount,a, amount-a])
                        acc += tmp
                        print(visited)
                _V[tuple(state)] = [acc,rec]
                # print(visited)
            return _V[tuple(state)]

sol =Solution()
print(sol.change(5,[1,2,5]))