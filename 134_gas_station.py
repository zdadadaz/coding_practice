class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        tot = 0
        surplus = 0
        S = 0
        for i in range(len(gas)):
            diff = gas[i] - cost[i]
            tot += diff
            surplus += diff
            if surplus <0:
                surplus = 0
                S=i+1
        if tot < 0:
            return -1
        return S