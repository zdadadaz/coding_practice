class Solution:
    def partition(self, s: str) -> List[List[str]]:
        pal = []
        visited = []
        num = 0
        self.dfs(s, pal, visited, num)
        return visited 
    
    def dfs(self, s, pal, visited, num):
        n = len(s)
        if num == n:
            # use deep copy for list
            x = pal.copy()
            visited.append(x)
            return
        
        for i in range(1, n + 1):
            if num + i > n:
                break
            if self.isPalindrome(s, num, num + i - 1):
                pal.append(s[num:num+i])
                self.dfs(s, pal, visited, num+i)
                pal.pop() # need pop, otherwise it will keep all the time

        
    def isPalindrome(self, string: str, low: int, high: int): 
        while low < high: 
            if string[low] != string[high]: 
                return False
            low += 1
            high -= 1
        return True
        
