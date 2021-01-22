class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        n = len(people)
        lt = 0
        rt = n-1
        cnt = 0
        while lt < rt:
            # if heaviest people cannot add with lightest one, then heavest one should be alone 
            if people[lt]+people[rt]>limit:
                rt-=1   
            else:
            # if they can pack together, then add one boat
                lt +=1
                rt -=1
            cnt += 1
                
        if lt == rt:
            return cnt+1
        return cnt