#Question: https://pynative.com/python-object-oriented-programming-oop-exercise/#h-oop-exercise-6-class-inheritance

class Vehicle():
    color = 'white'
    def __init__(self, name, max_speed, mileage, capacity) -> None:
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
        self.capacity = capacity

    def set_seating_capacity(self, capacity):
        return f'The seating capacity of a {self.name} is {capacity} passengers.'

    def get_fare(self):
        return self.capacity*100

# class Vehicle():
#     pass

class Bus(Vehicle):
    def __init__(self, name, max_speed, mileage, capacity) -> None:
        super().__init__(name, max_speed, mileage, capacity)

    def set_seating_capacity(self, capacity=50):
        return super().set_seating_capacity(capacity)
    
    def get_fare(self):
        final_amount = super().get_fare() + (.1*super().get_fare())
        return final_amount

class Car(Vehicle):
    def __init__(self, name, max_speed, mileage, capacity=None) -> None:
        super().__init__(name, max_speed, mileage, capacity)

bus1 = Bus('School Volvo', 180, 12, 50)
car1 = Car('Audi Q5', 240, 18)

print('Color:', bus1.color, '\nVehicle Name:', bus1.name, '\nSpeed:', bus1.max_speed, '\nMileage:', bus1.mileage)
print(bus1.set_seating_capacity())

print('Color:', car1.color, '\nVehicle Name:', car1.name, '\nSpeed:', car1.max_speed, '\nMileage:', car1.mileage)

print('Total bus fare is:', bus1.get_fare())

print(isinstance(bus1, Vehicle))