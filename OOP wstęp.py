
#class Car:
#    def __init__(self, color, mileage):
#        self.color=color
#        self.mileage=mileage
#
#    def __str__(self):
#        return f"The {self.color} car has {self.mileage} miles"
#
#    def ignite(self):
#        print("Brrrrum! The car has been ignited")

#class Kia(Car):
#    def __init__(self, color, mileage, mark):
#        self.mark=mark
#        Car.__init__(self, color, mileage)

#car_1=Kia("red", 10000, "Picanto")
#print(car_1)
#print(f"It's {car_1.mark}!")
#car_1.ignite()


class Dog:
    species="Canis familiaris"
    def __init__(self, name, age):
        self.name=name
        self.age=age

        
    def __str__(self):
        return f"{self.name} is {self.age} years old."
    
    def speak(self, sound):
        return f"{self.name} said {sound}"
    
    def roll(self, dist=20):
        return f"{self.name} rolled {dist} meters"
    

class Dachshund(Dog):
    def speak(self, sound="Hau"):
        return f"{self.name}, dachshund, says \"{sound}!\""

class Terrier(Dog):
    def speak(self, sound="Woof"):
        return f"{self.name}, terrier, says \"{sound}!\""

class Bulldog(Dog):
    def speak(self, sound="I torn my owners' child to pieces"):
        return f"{self.name}, bulldog, says \"{sound}!\""
    
class GoldenRetriever(Dog):
    def speak(self, sound="Bark"):
        return super().speak(sound)
    
    def roll(self, dist=30):
        return super().roll(dist)
   
miles = Terrier("Miles", 4,)
buddy = Dachshund("Buddy", 9,)
jack = Bulldog("Jack", 3)
anthony=GoldenRetriever("Anthony", 5)

print(anthony.speak())
print(buddy.speak())
print(jack.speak())
print(miles.speak())
print(miles.roll())
print(anthony.roll())
