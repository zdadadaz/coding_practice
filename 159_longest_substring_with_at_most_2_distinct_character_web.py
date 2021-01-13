class Solution:
    """
    @param s: a string
    @return: the length of the longest substring T that contains at most 2 distinct characters
    """
    def lengthOfLongestSubstringTwoDistinct(self, s):
        # Write your code here
        ans = 0
        Map = {}
        r = 0
        l = 0
        while r < len(s):
            if len(Map) <= 2:
                Map[s[r]] = r
                r += 1
            if len(Map) > 2:
                left = len(s)
                for i in Map.values():
                    left = min(left, i)
                Map.pop(s[left])
                l = left + 1
            ans = max(ans, r - l)
        return ans

    