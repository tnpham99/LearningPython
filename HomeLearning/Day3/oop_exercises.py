#Question: https://pynative.com/python-object-oriented-programming-oop-exercise/#h-oop-exercise-6-class-inheritance

class Vehicle():
    color = 'white'
    def __init__(self, name, max_speed, mileage, capacity) -> None:
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
        self.capacity = capacity

    def get_seating_capacity(self):
        return f'The seating capacity of a {self.name} is {self.capacity} passengers.'

    def get_fare(self):
        return self.capacity*100

# class Vehicle():
#     pass

class Bus(Vehicle):
    def __init__(self, name, max_speed, mileage, capacity=50) -> None:
        super().__init__(name, max_speed, mileage, capacity)

    def get_seating_capacity(self):
        return super().get_seating_capacity()
    
    def get_fare(self):
        final_amount = super().get_fare() + (.1*super().get_fare())
        return final_amount
class Car(Vehicle):
    def __init__(self, name, max_speed, mileage, capacity) -> None:
        super().__init__(name, max_speed, mileage, capacity)

bus1 = Bus('School Volvo', 180, 12)
car1 = Car('Audi Q5', 240, 18, 4)

print('Color:', bus1.color, '\nVehicle Name:', bus1.name, '\nSpeed:', bus1.max_speed, '\nMileage:', bus1.mileage)
print(bus1.get_seating_capacity())

print('Color:', car1.color, '\nVehicle Name:', car1.name, '\nSpeed:', car1.max_speed, '\nMileage:', car1.mileage)

print('Total bus fare is:', bus1.get_fare())

print(isinstance(bus1, Vehicle))