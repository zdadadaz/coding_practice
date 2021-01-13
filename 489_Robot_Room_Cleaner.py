import copy
import numpy as np
class Solution():
	def clean_room(self, room, row, col):
		start = (row, col)
		visited =[]
		self.dfs(start, room, visited)
		tmp = copy.deepcopy(room)
		for i in visited:
			tmp[i[0]][i[1]] = 0

		print(sum(np.array(tmp)))


	def dfs(self, start, room, visited):
		queue = []
		queue.append(start)
		while len(queue) != 0:
			cur = queue.pop()
			visited.append((cur))
			for i in self.successor(cur, room):
				if i not in visited:
					queue.append(i)
	
	def successor(self, pos, room):
		succces = []
		if self.isValid((pos[0]+1, pos[1]), room):
			succces.append((pos[0]+1, pos[1]))
		if self.isValid((pos[0]-1, pos[1]), room):	
			succces.append((pos[0]-1, pos[1]))
		if self.isValid((pos[0], pos[1]-1), room):
			succces.append((pos[0], pos[1]-1))
		if self.isValid((pos[0], pos[1]+1), room):
			succces.append((pos[0], pos[1]+1))
		return succces

	def isValid(self, pos, room):
		row = len(room)
		col = len(room[0])
		if pos[0] < 0 or pos[0]>=row:
			return False
		if pos[1] < 0 or pos[1]>=col:
			return False
		if room[pos[0]][pos[1]] == 0:
			return False
		return True


room = [
[1,1,1,1,1,0,1,1],
[1,1,1,1,1,0,1,1],
[1,0,1,1,1,1,1,1],
[0,0,0,1,0,0,0,0],
[1,1,1,1,1,1,1,1]
]
row = 1
col = 3
sol = Solution()
print(sol.clean_room(room,row, col))