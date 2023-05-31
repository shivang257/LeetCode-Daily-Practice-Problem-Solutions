class UndergroundSystem:

    def __init__(self):
        self.checkInMap = {}  # Uid - [StationName, Time]
        self.routeTotalTime = defaultdict(int)
        self.routeCount = defaultdict(int)

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.checkInMap[id] = [stationName, t]

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        checkIn = self.checkInMap.pop(id)  # Pop after using it which will not make HashTable big
        routeName = (checkIn[0], stationName)
        
        self.routeTotalTime[routeName] += t - checkIn[1]
        self.routeCount[routeName] += 1

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        routeName = (startStation, endStation)
        return self.routeTotalTime[routeName] / self.routeCount[routeName]