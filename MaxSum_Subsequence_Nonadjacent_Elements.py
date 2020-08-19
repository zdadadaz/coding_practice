def find_max_sum_nonadjacent(a):
  #TODO: Write - Your - Code
  tmp = [0] * len(a)
  tmp[0] = 1 # weird
  max_sum = tmp[0]
  for i in range(1,len(a)):
    max_sum = max(max_sum,tmp[i-1])
    if i > 1:
      max_sum = max(max_sum,tmp[i-2]+a[i])
    tmp[i] = max_sum    
  return max_sum

def find_max_sum_nonadjacent2(a):
  if len(a) == 0:
    return 0
  inc = exc = 0
  for i in a:
    tmp = inc
    inc = max(exc+i,inc)
    exc = tmp
  return max(inc,exc)

inp = [0,2,0]
# print(find_max_sum_nonadjacent([0,0,0]))
# print(find_max_sum_nonadjacent2([0,0,0,0]))
assert find_max_sum_nonadjacent(inp)==find_max_sum_nonadjacent2(inp), 'should be the same'