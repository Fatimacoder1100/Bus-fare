class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

class Bus(Vehicle):
    pass

school_bus = Bus("School Volvo", 80, 20)
fare_per_km = 10
distance = float(input("Enter distance in km: "))
total_fare = distance * fare_per_km

print("Vehicle Name:", school_bus.name)
print("Speed:", school_bus.max_speed)
print("Mileage:", school_bus.mileage)
print("Total Fare:", total_fare, "rupees")