class Dog: #the classe Dog and its attributes (name, age, breed, color) do not contain any data as of now. They just define what it is a dog. It is a blueprint of the Dog. In other words: it tells us what we need to construct a dog
    species = "Canis familiaris" # this is a class attribute (different than the instance attribute). This means that the species is applicable to ALL Dogs objects, regardless of their other characteristics

    def __init__(self, name, age): #remember name and age are parameters
        self.name = name
        self.age = age

    #after creating the Dog instances (objects), their attributes are accessed using dot notation
    #miles.name
    #miles.age
    #Instance methods are functions defined inside a class and can only call on an instance of that class.
    def description(self): #this instance method returns a str with the name and the age of the dog
        return f"{self.name} is {self.age} years old"

    def speak(self, sound): #this instance method has one paramenter (sound) and returns a str with the name of the dog and the sound it makes.
        return f"{self.name} says {sound}"
    
    
   # """
    #def __init__(self, name, age, breed, color): #the init method is where we define the Class properties(parameters). The first variable #will always be "self"
     #   self.name = name #creates an attribute called name and assignes the value of the name parameter to it (the value will be at a later stage. Remember that now we're just creating the blueprint, not the actual data). The attributes created in __init__ are called instance attributes (different than class attributes which are created outside the init method)
      #  self.age = age
       # self.breed = breed
        #self.color = color
    #"""