class vehicle:
    def maxspeed(self):
        pass

class BMW(vehicle):
    def maxspeed(self):
        return "BMW max speed is 215 MPH"
    
class ferrari(vehicle):
    def maxspeed(self):
        return "ferrari max speed is 250 MPH"
    
obj=[BMW(),ferrari()]
for vehicle in obj:
    print(vehicle.maxspeed())