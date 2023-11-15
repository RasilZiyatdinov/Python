class Load:
    def __init__(self, weight):
        self.weight = weight

    def __str__(self):
        return f"Груз массой {self.weight} кг"

class Cable:
    def __init__(self, length):
        self.length = length

    def __str__(self):
        return f"Кабель длиной {self.length} м"

class Crane:
    def __init__(self, max_load, max_cable_length):
        self.load = None
        self.cable = Cable(0)
        self.max_load = max_load
        self.max_cable_length = max_cable_length

    def __str__(self):
        if self.load is not None:
            return f"Кран: {self.load}, {self.cable}"
        else:
            return "Кран без груза"

    def lift(self, load):
        if self.load is None and load.weight <= self.max_load and load.weight * 2 <= self.max_cable_length:
            self.load = load
            self.cable = Cable(load.weight * 2)
        else:
            print("Невозможно поднять груз из-за ограничений по весу или длине кабеля")

    def lower(self):
        if self.load is not None:
            self.load = None
            self.cable = Cable(0)
        else:
            print("Нет груза для опускания")

    def __add__(self, other_crane):
        new_crane = Crane(self.max_load, self.max_cable_length)
        if self.load is not None and other_crane.load is not None:
            new_load = Load(self.load.weight + other_crane.load.weight)
            new_crane.lift(new_load)
        return new_crane

    def __sub__(self, other_crane):
        new_crane = Crane(self.max_load, self.max_cable_length)
        if self.load is not None:
            new_load = Load(self.load.weight - other_crane.load.weight)
            new_crane.lift(new_load)
        return new_crane


if __name__ == "__main__":
    crane1 = Crane(100, 10)
    crane2 = Crane(50, 10)

    load1 = Load(30)
    load2 = Load(5)

    crane1.lift(load1)
    crane2.lift(load2)

    print(crane1)
    print(crane2)

    crane3 = crane1 + crane2
    print(crane3)

    crane4 = crane1 - crane2
    print(crane4)