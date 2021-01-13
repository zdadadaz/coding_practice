class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans = 0
        for i in range(32):
            cnt = 0
            for j in nums:
                j = j>>i
                cnt += 1&j
            ans |= ((cnt%3) <<i)
        if ans >= 2 ** 31:
            ans -= 2 ** 32
        return ans
                    