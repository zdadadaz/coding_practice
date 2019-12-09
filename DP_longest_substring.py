
class solution:
    # method 1
    # O(n*m^2)
    def longest_substring(self,a,b):
        i,j = len(a)-1,len(b)-1
        return self.longest_substring_recur(a,b,i,j)

    def longest_substring_recur(self,a,b,i,j):
        if i ==0 or j ==0:
            return 0
        if a[i] == b[j]:
            return self.longest_substring_recur(a,b,i-1,j-1)+1
        else:
            return self.longest_substring_recur(a,b,i-1,j-1)
    
    # method 2 memory and recurrence
    # complexity O(m*n)/ space O(m*n)
    def longest_substring_mem_recur(self, a,b):
        sa,sb = len(a)+1,len(b)+1
        arr = [[0 for k in range(sa)] for l in range(sb)]
        i,j = sa-1,sb-1
        return self.longest_substring_mem_recur(a,b,i,j,arr)
    
    def longest_substring_mem_recur(self,a,b,i,j, arr):
        result = 0
        if arr[j][i] != 0:
            return arr[j][i]
        if a[i-1] == b[j-1]:
            arr[j][i] = self.longest_substring_recur(a,b,i-1,j-1)+1
            return arr[j][i]
        else:
            max(self.longest_substring_recur(a,b,i-1,j),self.longest_substring_recur(a,b,i,j-1)
        return result 
        
    # method 3 
    # Buttom up 
    def longest_substring_buttomup(self,a,b):
        sa,sb = len(a)+1,len(b)+1
        # arr = [[0]*sa]*sb, doesnt work, because []*sb is duplicate reference
        arr = [[0 for k in range(sa)] for l in range(sb)] 
        result = 0
        for i in range(1,sa):
            for j in range(1,sb):
                if a[i-1] == b[j-1]:
                    arr[j][i] = arr[j-1][i-1] + 1
                    result = max(result,arr[j][i])
                else:
                    arr[j][i] = 0
        return result

a = "OldSite:GeeksforGeeks.org"
b = "NewSite:GeeksQuiz.com"
sol = solution()
print(sol.longest_substring_buttomup(a,b))