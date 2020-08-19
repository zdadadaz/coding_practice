# over time

import copy
class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        N = round(len(costs)/2)
        p = [-1]*N*2 # 0,1 for city A and B
        _V={}
        return self.recur(0,p,N, costs,_V, [0]*2)
    
    def check_city(self, p, N, a):
        count=[0]*2
        for i in p:
            if i == 0:
                count[0] += 1
            elif i == 1:
                count[1] += 1
        if (count[a] + 1) >N:
            return False
        else:
            return True
    
    #stage:i client
    #state:p people in each city
    #action:j assign i people in p city
    def recur(self,i, p, N,costs,_V, count):
        if i == (N*2) and (-1 not in p):
            return sum(costs[client][city] for client, city in enumerate(p)) 
        else:
            if tuple(p) not in _V:
                out=[]
                for j in range(2):
                    if (count[j] + 1) <= N:
                        p_tmp = copy.deepcopy(p)
                        p_tmp[i] = j
                        count_tmp = copy.deepcopy(count)
                        count_tmp[j] +=1
                        out.append(self.recur(i+1, p_tmp, N, costs, _V, count_tmp) )
                _V[tuple(p)] = min(out)
                print(_V)
            return _V[tuple(p)]
            
