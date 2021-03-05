class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits[-1] += 1
        prev = 0
        for i in range(len(digits)-1,-1,-1):
            if digits[i]+prev > 9:
                digits[i] = 0
                prev = 1
            else:
                digits[i] += prev
                return digits
        return [1] + digits
        
                