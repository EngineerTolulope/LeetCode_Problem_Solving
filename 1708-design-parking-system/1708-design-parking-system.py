class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.remaining_spaces = {1 : big, 2 : medium, 3 : small}

    def addCar(self, carType: int) -> bool:
        space = self.remaining_spaces[carType]
        if space > 0:
            self.remaining_spaces[carType] -= 1
            return True
        return False
        


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)