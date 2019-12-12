# The basic idea of Kadane's algorithm is to scan the entire array 
# and at each position find the maximum sum of the subarray ending there. 
# This is achieved by keeping a current maximum for the current array index and a global maximum. 
# The algorithm is as follows:

def find_max_sum_sub_array(A):
  #TODO: Write - Your - Code
  cur_max = A[0]
  glb_max = A[0]
  for i in range(1,len(A)):
    if cur_max < 0:
      cur_max = A[i]
    else:
      cur_max += A[i]
    if glb_max < cur_max:
      glb_max = cur_max

  return glb_max  