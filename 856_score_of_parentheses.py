class Solution:
    # best O(N), worst O(N^2)
    def scoreOfParentheses(self, S: str) -> int:
        def recursion(l,r):
            if r-l == 1:
                return 1
            b = 0
            for i in range(l,r): # ()
                if S[i] == '(':
                    b+=1
                else:
                    b-=1
                if b == 0:
                    return recursion(l,i)+recursion(i+1,r)
            
            return 2 * recursion(l+1,r-1)
        return recursion(0,len(S)-1)

    # O(N)
    def scoreOfParentheses_count(self, S: str) -> int:
        cnt = 0
        res = 0
        for i in range(len(S)-1):
            if S[i] == '(':
                cnt += 1
            else:
                cnt -= 1
            if S[i] == '(' and S[i+1]==')':
                res += 1<<(cnt-1)
        return res