# Joshua Hamaker        04/10/2025
# Lecture notes - 04/10

## Inheritence


class Animal:
    def __init__(self, name: str, age: int, color: str) -> None:
        self.name = name
        self.age = age
        self.color = color
    def __str__(self) -> str:
        return (f"Name: {self.name}, Age: {str(self.age)}, Color: {self.color}")
    def speak(self):
        return "Hello!"
    def getName(self):
        return self.name


class Robot:
    def __init__(self, power: int) -> None:
        self.power = power
    def beep(self) -> str:
        return "beep " * self.power


class Cat(Animal):
    def speak(self):
        return "Meow! " * self.age


class Dragon(Animal):
    def speak(self):
        return "Hi" + "s" * self.age + "! "


class Werewolf(Animal):
    def speak(self):
        return "G" + "r" * self.age + "! "


class Tiger(Cat, Robot):
    def __init__(self, name: str, age: int, color: str, strength: int, power: int) -> None:
        Cat.__init__(self, name, age, color)
        Robot.__init__(self, power)
        self.strength = strength
    def __str__(self) -> str:
        return super().__str__() + f", Strength: {str(self.strength)}"
    def yell(self):
        return "Roar! " * self.strength


c1 = Cat("Patches", 10, "Orange")
c2 = Cat("Garfield", 4, "Red")
print(c1)
print(c1.speak())
print(c2)
print(c2.speak())

d1 = Dragon("Clay", 12, "Brown")
print(d1)
print(d1.speak())

w1 = Werewolf("Edward", 35, "Silver")
print(w1)
print(w1.speak())

t1 = Tiger("Tigger", 5, "Orange", 2, 10)
print(t1)
print(t1.speak())
print(t1.yell())
print(t1.beep())

print("-----------------------------------------------------")

animals = []
animals.append(Animal("Jeffery", 22, "Pink"))
animals.append(Cat("Oreo", 3, "black"))
animals.append(Dragon("Toothless", 39, "Black"))
animals.append(Werewolf("Stan", 61, "Grey"))
animals.append(Tiger("Tom", 12, "Blue", 3, 2))

for a in animals:
    print(f"{a.getName()} says {a.speak()}")