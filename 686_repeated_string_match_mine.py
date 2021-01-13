class Solution:
    def repeatedStringMatch(self, A: str, B: str):
        AinB = self.check_A_in_B(A,B)
        if AinB:
            count = 1          
            Atmp = A
            while not self.check_A_in_B(B,Atmp):
                Atmp = Atmp+A
                count += 1
            return count
        return -1
                
        
    def check_A_in_B(self, A, B):
        if len(A) == 0 or len(B) == 0 or len(A)>len(B):
            return False
        for i in range(len(B)):
            flag = True
            for j in range(len(A)):
                if i+j>=len(B) or B[i+j] != A[j]:
                    flag = False
                    break
            if flag:
                return True
        return False

sol = Solution()
A = 'abcd'
B = 'cdabcdab'
output = sol.repeatedStringMatch(A,B)
# print(A*2)