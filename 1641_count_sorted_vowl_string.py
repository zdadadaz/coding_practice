class Solution:
    def countVowelStrings(self, n: int) -> int:
        arr = [1] * 5
        for i in range(n-1):
            sum_arr = sum(arr)
            for j in range(5):
                tmp = arr[j]
                arr[j] = sum_arr
                sum_arr -= tmp
        return sum(arr)
            
        