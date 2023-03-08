from pets import Pet

class Ninja:
# implement __init__( first_name , last_name , treats , pet_food , pet )
    def __init__(self, first_name, last_name,  pet, treats, pet_food):
        self.first_name = first_name
        self.last_name = last_name
        self.pet = pet
        self.treats = treats
        self.pet_food = pet_food

# implement the following methods:
# walk() - walks the ninja's pet invoking the pet play() method
# feed() - feeds the ninja's pet invoking the pet eat() method
# bathe() - cleans the ninja's pet invoking the pet noise() method
    def walk(self):
        print(f'{self.first_name} is walking {self.pet.name}!')
        self.pet.play()
    def feed(self):
        print(f'{self.first_name} is feeding {self.pet.name}!')
        self.pet.eat()
    def bathe(self):
        print(f'{self.first_name} is bathing {self.pet.name}!')
        self.pet.noise()

pet_1 = Pet('Hugin', 'Raven', 'Fly')
ninja_1 = Ninja('Itachi', 'Uchiha', pet_1, 'candy', 'kibble')

ninja_1.feed()
ninja_1.walk()
ninja_1.bathe()