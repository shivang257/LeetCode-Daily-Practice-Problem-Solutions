class SeatManager:
    def __init__(self, n: int):
        self.lis = list(range(1,n+1))
        heapify(self.lis)
        
    def reserve(self) -> int:
        return heappop(self.lis)
    
    def unreserve(self, seatNumber: int) -> None:
        heappush(self.lis,seatNumber)