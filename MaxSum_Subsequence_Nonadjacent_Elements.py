def find_max_sum_nonadjacent(a):
  #TODO: Write - Your - Code
  tmp = [0] * len(a)
  tmp[0] = 1
  max_sum = tmp[0]
  for i in range(1,len(a)):
    max_sum = max(max_sum,tmp[i-1])
    if i > 1:
      max_sum = max(max_sum,tmp[i-2]+a[i])
    tmp[i] = max_sum    
  return max_sum