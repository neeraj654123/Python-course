# Single Inheritance

# Base class representing a generic vehicle
class Vehicle:                  # Vehicle is a parent class of Car 
    company = "Toyota"
# Initialize vehicle with mileage, wheel count, and seat count
    def __init__(self, mileage, n_wheels,n_seats):
        # Initialize vehicle with mileage, wheel count, and seat count.

        print("init of vehicle")
        self.mileage = mileage
        self.n_wheels = n_wheels
        self.n_seats = n_seats

    def vehicle_info(self):
        print("Company:", self.company)
        print("Mileage:", self.mileage)
        print("Number of wheels:", self.n_wheels)
        print("Number of seats:", self.n_seats)

class Car(Vehicle):                # Car is a child class of Vehicle 
    Model="ABC123"
    def __init__(self, car_type, drive_type, mileage=15, n_wheels=4, n_seats=5):
        # Car constructor with defaults for inherited vehicle attributes.
        print("init of Car")
        # super().__init__(mileage, n_wheels, n_seats) calls Vehicle.__init__() and initializes parent class attributes
        super().__init__(mileage, n_wheels, n_seats)
        self.car_type = car_type
        # Type of the car (e.g., Sedan, SUV).
        self.drive_type = drive_type
        # Transmission type (Manual or Automatic).

car = Car("Sedan", "Manual")
print(car.company) 
print(car.Model)
print(car.mileage)