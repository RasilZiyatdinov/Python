class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def __str__(self):
        return f"{self.year} {self.make} {self.model}"
    
    def __repr__(self):
        return f"Vehicle('{self.make}', '{self.model}', {self.year})"
    
    def __eq__(self, other):
        if isinstance(other, Vehicle):
            return self.year == other.year and self.make == other.make and self.model == other.model
        return False

    def __ne__(self, other):
        if isinstance(other, Vehicle):
            return not self.__eq__(other)
        return False

    def __lt__(self, other):
        if isinstance(other, Vehicle):
            return (self.year, self.make, self.model) < (other.year, other.make, other.model)
        return False

    def __gt__(self, other):
        if isinstance(other, Vehicle):
            return (self.year, self.make, self.model) > (other.year, other.make, other.model)
        return False

    def __le__(self, other):
        if isinstance(other, Vehicle):
            return self.__lt__(other) or self.__eq__(other)
        return False

    def __ge__(self, other):
        if isinstance(other, Vehicle):
            return self.__gt__(other) or self.__eq__(other)
        return False

class Car(Vehicle):
    def __init__(self, make, model, year, num_doors):
        super().__init__(make, model, year)
        self.num_doors = num_doors

    def __str__(self):
        return f"{super().__str__()} with {self.num_doors} doors"
    
    def __repr__(self):
        return f"Car('{self.make}', '{self.model}', {self.year}, {self.num_doors})"
    
    def __eq__(self, other):
        if isinstance(other, Car):
            return super().__eq__(other) and self.num_doors == other.num_doors
        return False
    
    def __ne__(self, other):
        if isinstance(other, Car):
            return super().__ne__(other) or self.num_doors != other.num_doors
        return False
    
    def __lt__(self, other):
        if isinstance(other, Car):
            return super().__lt__(other) and self.num_doors < other.num_doors
        return False

    def __gt__(self, other):
        if isinstance(other, Car):
            return super().__gt__(other) and self.num_doors > other.num_doors
        return False

    def __le__(self, other):
        if isinstance(other, Car):
            return super().__le__(other) and self.num_doors <= other.num_doors
        return False

    def __ge__(self, other):
        if isinstance(other, Car):
            return super().__ge__(other) and self.num_doors >= other.num_doors
        return False



class SportsCar(Car):
    def __init__(self, make, model, year, num_doors, top_speed):
        super().__init__(make, model, year, num_doors)
        self.top_speed = top_speed

    def __str__(self):
        return f"{super().__str__()} with a top speed of {self.top_speed} mph"
    
    def __repr__(self):
        return f"SportsCar('{self.make}', '{self.model}', {self.year}, {self.num_doors}, {self.top_speed})"
    
    def __eq__(self, other):
        if isinstance(other, SportsCar):
            return super().__eq__(other) and self.top_speed == other.top_speed
        return False
    
    def __ne__(self, other):
        if isinstance(other, SportsCar):
            return super().__ne__(other) or self.top_speed != other.top_speed
        return False
    
    def __lt__(self, other):
        if isinstance(other, SportsCar):
            return super().__lt__(other) and self.top_speed < other.top_speed
        return False

    def __gt__(self, other):
        if isinstance(other, SportsCar):
            return super().__gt__(other) and self.top_speed > other.top_speed
        return False

    def __le__(self, other):
        if isinstance(other, SportsCar):
            return super().__le__(other) and self.top_speed <= other.top_speed
        return False

    def __ge__(self, other):
        if isinstance(other, SportsCar):
            return super().__ge__(other) and self.top_speed >= other.top_speed
        return False
    

if __name__ == "__main__":
    vehicle1 = Vehicle("МТЗ", "80", 1990)
    vehicle2 = Vehicle("Kawasaki Ninja", "H2", 2023)
    vehicle3 = Vehicle("Kawasaki Ninja", "H2", 2023)

    car1 = Car("Audi", "q3", 2018, 5)
    car2 = Car("Audi", "q3", 2019, 6)

    sportcar1 = SportsCar("Porsche", "911", 2021, 2, 182)
    sportcar2 = SportsCar("Bugatti", "Chiron", 2020, 2, 304)

    print(str(vehicle1))
    print(str(car1))
    print(str(sportcar1))
    print(repr(vehicle1))
    print(repr(car1))
    print(repr(sportcar1))
    print()

    print(vehicle1 == vehicle2)
    print(car1 != sportcar1)
    print(vehicle2 == sportcar2)
    print(sportcar1 > sportcar2)
    print(car1 < vehicle1)
    print(vehicle2 == vehicle3)
    print(car1 <= car2)

