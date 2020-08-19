# start from taller one
class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key = lambda x: (-x[0],x[1])) 
        out = []
        for i in people:
            out.insert(i[1],i)
        return out