class Solution:
    """
    @param s: a string
    @return: the length of the longest substring T that contains at most 2 distinct characters
    """
    def lengthOfLongestSubstringTwoDistinct(self, s):
        # Write your code here
        counter = [0]*52
        N = len(s)
        left = 0
        number_distinct = 0
        longest_number = 0
        for i in range(N):
            number_distinct = self.addChar(s[i], counter, number_distinct)
            while number_distinct > 2:
                number_distinct = self.removeChar(s[left], counter, number_distinct)
                left += 1
            longest_number = max(longest_number, i - left + 1)
            
        return longest_number
            
        
    def addChar(self, ch, counter, number_distinct):
        index = ord(ch)-ord('a')
        if index < 0:
            index = ord(ch)-ord('A') + 26
        if counter[index] == 0:
            number_distinct += 1
        counter[index] += 1
        return number_distinct
    
    def removeChar(self, ch, counter, number_distinct):
        index = ord(ch)-ord('a')
        if index < 0:
            index = ord(ch) - ord('A') + 26
        counter[index] -= 1
        if counter[index] == 0:
            number_distinct -= 1
        return number_distinct