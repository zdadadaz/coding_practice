class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.que = []
        

    def push(self, x: int) -> None:
        self.que.append(x)

    def pop(self) -> None:
        return self.que.pop()

    def top(self) -> int:
        return self.que[-1]

    def getMin(self) -> int:
        return min(self.que)


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

class MinStack_min_stack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.que = []
        self.min = []

    def push(self, x: int) -> None:
        if len(self.min)==0 or x < self.min[-1]:
            self.min.append(x)
        else:
            self.min.append(self.min[-1])
        self.que.append(x)

    def pop(self) -> None:
        self.min.pop()
        return self.que.pop()

    def top(self) -> int:
        return self.que[-1]

    def getMin(self) -> int:
        return self.min[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()