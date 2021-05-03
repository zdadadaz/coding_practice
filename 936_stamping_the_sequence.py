class Solution:
    def movesToStamp(self, stamp: str, target: str) -> List[int]:
        n,s = len(target),len(stamp)
        res = []
        allstar = ''.join(['*' for z in range(s)])
        tot= 0 # total number of *
        while tot < n:
            tot_tmp = tot
            for i in range(n-s+1):
                cur = target[i:(i+s)]
                if cur==allstar:
                    continue
                # check cur == stamp or not
                flag = True
                for j in range(s):
                    if cur[j] != stamp[j] and cur[j]!='*':
                        flag = False
                        break
                # cur==stamp, then make target "*" and append to results
                if flag:
                    cur_star_num = sum([1 for z in cur if z=='*'])
                    tot += s-cur_star_num
                    target = target[:i] + allstar + target[(i+s):]
                    res.append(i)
            if tot==tot_tmp:
                return []
        return res[::-1]