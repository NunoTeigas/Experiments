class Dog: 
    species = "Canis familiaris"

    def __init__(self, name, age): #remember name and age are parameters
        self.name = name
        self.age = age

    def __str__(self): #this instance method returns a str with the name and the age of the dog
        return f"{self.name} is {self.age} years old"

    def speak(self, sound): #this instance method has one paramenter (sound) and returns a str with the name of the dog and the sound it makes.
        return f"{self.name} says {sound}"