class Solution:
    def solve(self, board):
        """
        Do not return anything, modify board in-place instead.
        """
        if len(board)==0:
            return
        checked = [[0]*len(board[0]) for i in range(len(board))]
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == 'O' and checked[i][j] == 0:
                    self.dfs((i,j), board, checked)
                       
    def dfs(self,st, board,checked):
        from collections import deque
        que = deque()
        que.append(st)
        boundary = 0
        visited = []
        while len(que)>0:
            cur = que.pop()
            boundary = 1 if cur[0]==0 or cur[0] == len(board)-1 or cur[1]==0 or cur[1] == len(board[cur[0]])-1 else boundary
            visited.append(cur)
            for a in self.gen_conn(cur, board):
                if a not in visited:
                    que.append(a)
        for vi in visited:
            checked[vi[0]][vi[1]] = 1
            if boundary == 0:
                board[vi[0]][vi[1]] = "X"
            
    
    def gen_conn(self, cur, board):
        if cur[0]-1 >=0 and board[cur[0]-1][cur[1]] == "O":
            yield (cur[0]-1,cur[1])
        if cur[0]+1 <len(board) and board[cur[0]+1][cur[1]] == "O":
            yield (cur[0]+1,cur[1])
        if cur[1]-1 >=0 and board[cur[0]][cur[1]-1] == "O":
            yield (cur[0],cur[1]-1)
        if cur[1]+1 <len(board[cur[0]]) and board[cur[0]][cur[1]+1] == "O":
            yield (cur[0],cur[1]+1)
        
sol = Solution()
print(sol.solve([["O","O","O","O"],["O","O","O","O"],["O","O","X","O"],["O","O","O","X"]]))