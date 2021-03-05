class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        n = len(candyType)
        c = Counter(candyType)
        return n//2 if len(c)> n//2 else len(c)
        