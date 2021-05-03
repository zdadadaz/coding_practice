class Solution:
    def originalDigits(self, s: str) -> str:
        c = Counter(s)
        one = []
        two = []
        three = []
        letter = {0:Counter('zero'),1:Counter('one'),2:Counter('two'),3:Counter('three'),4:Counter('four'),5:Counter('five'),6:Counter('six'),7:Counter('seven'),8:Counter('eight'),9:Counter('nine')}
        one_m = {'z':0, 'w':2, 'u':4, 'x':6, 'g':8}
        two_m = {'o':1, 't':3, 'f':5, 's':7}
        three_m={'n':9}
        def checkin(m, arr,c):
            for i in m:
                while i in c and c[i]>0:
                    flag = True
                    for j in letter[m[i]].keys():
                        if c[j]<=0:
                            flag =False
                            break
                    if flag:
                        c = c-letter[m[i]] 
                        arr.append(m[i])
            return c
        c = checkin(one_m, one,c)
        c = checkin(two_m, two,c)
        res = []
        i =j=0
        n1,n2 = len(one),len(two)
        while i<n1 or j < n2:
            one_tmp = one[i] if i<n1 else float('inf') 
            two_tmp = two[j] if j<n2 else float('inf') 
            if one_tmp < two_tmp:
                res.append(str(one_tmp))
                i+=1
            else:
                res.append(str(two_tmp))
                j+=1
        c = checkin(three_m, three,c)
        res += [str(9)]*len(three)
        return ''.join(res)

    def originalDigits_count_times(self, s: str) -> str:
        c = Counter(s)
        one_m = {'z':0, 'w':2, 'u':4, 'x':6, 'g':8}
        two_m = {'o':1, 't':3, 'f':5, 's':7}
        three_m={'n':9}
        n = [0]*10
        n[0] = c['z']
        n[2] = c['w']
        n[4] = c['u']
        n[6] = c['x']
        n[8] = c['g']
        n[1] = c['o']-n[0]-n[2]-n[4]
        n[3] = c['h']-n[8]
        n[5] = c['f']-n[4]
        n[7] = c['s']-n[6]
        n[9] = c['i']-n[5]-n[6]-n[8]
        res = []
        for i in range(10):
            res.append(str(i)*n[i])
        return ''.join(res)
        
        
        