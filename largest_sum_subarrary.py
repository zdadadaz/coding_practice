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


# Python program to find maximum contiguous subarray 
# Function to find the maximum contiguous subarray 
from sys import maxint 
def maxSubArraySum(a,size): 
	
	max_so_far = -maxint - 1
	max_ending_here = 0
	
	for i in range(0, size): 
    # keep add number to current sum
		max_ending_here = max_ending_here + a[i] 
    # compare with global sum
		if (max_so_far < max_ending_here): 
			max_so_far = max_ending_here 
    # only maintain the summation larger than 0
		if max_ending_here < 0: 
			max_ending_here = 0
	return max_so_far 

# Driver function to check the above function 
a = [-13, -3, -25, -20, -3, -16, -23, -12, -5, -22, -15, -4, -7] 
print "Maximum contiguous sum is", maxSubArraySum(a,len(a)) 

#This code is contributed by _Devesh Agrawal_ 

