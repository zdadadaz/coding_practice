class UndergroundSystem:

    def __init__(self):
        from collections import defaultdict
        self.avg = {}
        self.id = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        if id not in self.id:
            self.id[id] = [stationName, t]

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        if id in self.id:
            if (self.id[id][0], stationName) not in self.avg:
                self.avg[(self.id[id][0], stationName)] = [1, t-self.id[id][1]]
            else:
                self.avg[(self.id[id][0], stationName)][0] += 1
                self.avg[(self.id[id][0], stationName)][1] += t-self.id[id][1]
            del self.id[id]

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        if (startStation, endStation) in self.avg:
            return self.avg[(startStation, endStation)][1]/self.avg[(startStation, endStation)][0]


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)