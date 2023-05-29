class ParkingSystem:

    def __init__(self, big, medium, small):
        self.A = [big, medium, small]

    def addCar(self, carType):
        self.A[carType - 1] -= 1
        return self.A[carType - 1] >= 0