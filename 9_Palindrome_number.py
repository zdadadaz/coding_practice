class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = str(x)
        n = len(s)
        for i in range(n//2):
            if s[i]!= s[n-1-i]:
                return False
        return True

    def isPalindrome_reverse(self, x: int) -> bool:
        reverse = 0
        if x<0 or (x%10 ==0 and x != 0):
            return False
        while x> reverse:
            cur = x % 10
            reverse = reverse*10+cur
            x = x//10
        return reverse == x or x == reverse//10