class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == '1' and (i,j) not in visited:
                    self.dfs(grid, (i,j), visited)
                    count +=1
        return count
                
    def dfs(self, grid, cur_position, visited):
        new_poses = [(cur_position[0]+1, cur_position[1]),(cur_position[0]-1, cur_position[1]),(cur_position[0], cur_position[1]+1),(cur_position[0], cur_position[1]-1)]
        for pos in new_poses:
            if self.successor(pos, grid) and pos not in visited and grid[pos[0]][pos[1]] == '1':
                visited.add(pos)
                self.dfs(grid, pos, visited)

    def successor(self, position, grid):
        if position[0]<0 or position[0] >= len(grid):
            return False
        if position[1]<0 or position[1] >= len(grid[0]):
            return False
        return True