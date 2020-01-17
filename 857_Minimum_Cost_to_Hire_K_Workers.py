import heapq
class Solution:
    # O(N^2) over time limit, O(N)
    def mincostToHireWorkers(self, quality, wage, K):
        minWage = float("inf")
        for i in range(len(quality)):
            successes = self.successor(i, quality, wage)
            successes = sorted(successes)
            # print(str(i)+str(successes))
            wage_sum = wage[i]
            count = 1
            for j in range(len(successes)):
                if count >= K:
                    break
                wage_sum += successes[j]
                count += 1
            if count >= K:
                minWage = min(minWage, wage_sum)
        return minWage      
    
    def successor(self, idx, quality, wage):
        wages = []
        for i in range(len(quality)):
            newWorker_wage = float(quality[i])/quality[idx] * wage[idx]
            # print(str(newWorker_wage) + " "+str(wage[i]))
            if newWorker_wage < wage[i] or i == idx:
                continue
            wages.append(newWorker_wage)
        return wages

    # O(nlogn) time,O(n) space
    def mincostToHireWorkers_optimal(self, quality, wage, K):
        # calculate cost/quality ratio
        # quality sum * ratio = total wage
        workers = [[w/q,q] for w,q in zip(wage, quality)]
        # sorted rate can make sure the qsum * r is the smallest of the chosed q
        workers = sorted(workers)
        heap =[]
        qsum = 0
        minWage = float("inf")
        for i in range(len(workers)):
            r, q = workers[i]
            heapq.heappush(heap, -q)
            qsum += q
            if len(heap) > K:
                # remove maximal quality, which tend to need more wage than others
                tmp = heapq.heappop(heap)
                qsum += tmp
            if len(heap) == K:
                wageSum = r*qsum
                minWage = min(minWage, wageSum)
        return minWage




sol = Solution()
q = [10,20,5]
w = [70,50,30]
k = 2
print(sol.mincostToHireWorkers_optimal(q,w,k))
