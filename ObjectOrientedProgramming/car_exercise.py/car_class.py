class Car:

    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage

    def __str__(self): #this str method allows to display of objects when they-re passed to print()
        return f"The {self.color} car has {self.mileage:,} miles"
    
