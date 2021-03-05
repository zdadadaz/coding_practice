class FreqStack:
    # O(1), O(N)
    def __init__(self):
        from collections import defaultdict
        self.c = Counter()
        self.stack = defaultdict(list)
        self.maxfreq = 0

    def push(self, x: int) -> None:
        self.c[x] +=1 
        self.maxfreq = max(self.maxfreq, self.c[x])
        self.stack[self.c[x]].append(x)
        
    def pop(self) -> int:
        cand = self.stack[self.maxfreq].pop()
        self.c[cand] -= 1
        if not self.stack[self.maxfreq]:
            self.maxfreq -=1
        return cand

# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(x)
# param_2 = obj.pop()