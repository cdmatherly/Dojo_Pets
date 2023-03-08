class Pet:
# implement __init__( name , type , tricks ):
    def __init__(self, name, type, tricks):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.energy = 50
        self.health = 100
# implement the following methods:
# sleep() - increases the pets energy by 25
# eat() - increases the pet's energy by 5 & health by 10
# play() - increases the pet's health by 5
# noise() - prints out the pet's sound
    def sleep(self):
        self.energy += 25
    def eat(self):
        self.energy += 5
        self.health += 10
        print(f"{self.name}'s health is increased to {self.health} and energy is increased to {self.energy}!")
    def play(self):
        self.health += 5
        print(f"{self.name}'s health is increased to {self.health}!")
    def noise(self):
        print('**Caw**')