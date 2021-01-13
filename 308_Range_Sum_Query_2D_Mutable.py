import math
import numpy as np

# using sement_tree to make read and write -> O(long N)
# otherwise, O(N)
class Segment_tree_1d():
	def segment_tree_main(self, arr, row):
		st = self.construct_tree(arr)
		# print(arr)
		# print(st)
		# print("=== ")
		# self.update_tree(arr, st, 1, 6)
		# arr[1] = 6
		# print(arr)
		# print(st)
		return self.get_sum(st, 0, len(arr)-1, row[0], row[1], 0)


	def construct_tree(self, arr):
		xx = math.ceil(math.log2(len(arr)))
		max_len = 2* (int)(2**xx) - 1

		# print(max_len)
		st=[0]*max_len
		self.construct_tree_unit(st, 0, arr, 0, len(arr)-1)
		return st

	def construct_tree_unit(self, st, i, arr, ss, se):
		if ss==se:
			# print(i)
			st[i] = arr[ss]
			return arr[ss]
		mid = int((ss+se)/2)
		# mid = ss + (se -ss) // 2
		st[i] = self.construct_tree_unit(st, 2*i + 1, arr, ss,   mid) + \
				self.construct_tree_unit(st, 2*i + 2, arr, mid+1, se) 
		return st[i]
        
	def get_sum(self, st, ss, se, qs, qe, i):
		if qs <= ss and qe >= se: # q complete cover s
			return st[i]
		if qs > se or qe < ss: # no overlap
			return 0
		mid = int((ss+se)/2)
		return self.get_sum(st, ss, mid, qs, qe, 2*i+1) + \
			   self.get_sum(st, mid+1, se, qs, qe, 2*i+2)
	
	def update_tree(self, arr, st, i, value):
		diff = value - arr[i] 
		self.update_tree_unit(st, 0, arr, 0, len(arr)-1, i, diff)

	def update_tree_unit(self, st, si, arr, ss, se, i, diff):
		if i < ss or i > se:
			return
		st[si] += diff
		mid = int((ss+se)/2)
		if ss != se:
			self.update_tree_unit(st, si * 2 + 1, arr, ss, mid, i, diff)
			self.update_tree_unit(st, si * 2 + 2, arr, mid+1, se, i, diff)

class Segment_tree_2d(Segment_tree_1d):
	def segment_tree_main(self, arr, matrix):
		print(arr)
		st = self.construct_tree_2d(arr)
		print(st)
		return self.get_sum_2D(arr, st, matrix)

	def construct_tree_2d(self, arr):
		stemp = []
		xx = math.ceil(math.log2(len(arr)))
		max_len = 2 * (2 ** xx) - 1
		st = [None]* max_len
		for i in arr:
			stemp.append(self.construct_tree(i))
		self.construct_tree_2d_unit(stemp, 0, len(arr)-1, st, 0)
		return st
	
	def construct_tree_2d_unit(self, arr, ss, se, st, si):
		if ss==se:
			st[si] = arr[ss]
			return arr[ss]

		mid = int((ss+se)/2)
		st[si] = list(np.array(self.construct_tree_2d_unit(arr, ss, mid, st, si*2+1))+\
				 np.array(self.construct_tree_2d_unit(arr, mid+1, se, st, si*2+2)))
		return st[si]

	def get_sum_2D(self, arr, st, matrix):
		y = [matrix[0][0],matrix[1][0]]
		x = [matrix[0][1],matrix[1][1]]
		return self.get_sum_2D_unit(arr, 0, len(arr)-1, st, 0, y, x)

	def get_sum_2D_unit(self, arr,  ss, se, st, si, y, x):
		if y[0] <= ss and y[1] >=se: # y complete cover
			return self.get_sum(st[si], 0, len(arr[0])-1, x[0], x[1], 0)
		if y[0] > se or y[1] < ss:
			return 0
		mid = int((ss+se)/2)
		return self.get_sum_2D_unit(arr, ss, mid, st, si*2+1, y, x) + \
			   self.get_sum_2D_unit(arr, mid+1, se, st, si*2+2, y, x)

	# def update_tree_2D(self,)


	
# 1d testing
# sol = Segment_tree_1d()
# arr= [2,4,6,1,5,6,3]
# row = [1,3]
# print(sol.segment_tree_main(arr, row))


# 2d testing
sol = Segment_tree_2d()
arr= [[1,2,3,4], [5,6,7,8], [1,7,5,9],[3,0,6,2]]
matrix = [[1,0], [2,1]]
print(sol.segment_tree_main(arr, matrix))
