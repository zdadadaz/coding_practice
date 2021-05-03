class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers)-1
        while l < r:
            tot = numbers[l]+numbers[r]
            if tot == target:
                return [l+1, r+1]
            elif tot > target:
                r -= 1
            else:
                l += 1
        return -1