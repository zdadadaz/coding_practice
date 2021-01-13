class Solution():
    # method 1 memorization with recursion
    # O(n)
    def scoring_options_memorization(self,n):
        arr= [0]*(n+1)
        arr[0] = 1
        self.scoring_options_memorization_recur(n,arr)
        return arr[n]

    def scoring_options_memorization_recur(self,n,arr):
        if n < 0:
            return 0
        if arr[n] >0:
            return arr[n]
        arr[n] = self.scoring_options_memorization_recur(n-1,arr)  \
                + self.scoring_options_memorization_recur(n-2,arr) \
                + self.scoring_options_memorization_recur(n-4,arr)
        return arr[n]

    


sol = Solution()
A = 5
print(sol.scoring_options_memorization(A))