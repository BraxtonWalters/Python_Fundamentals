class Pet:

    # implement __init__( name , type , tricks ):
    def __init__(self, name, type, tricks):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.health = 50
        self.energy = 10

    # implement the following methods:
    # sleep() - increases the pets energy by 25
    def sleep(self):
        self.health += 25

    # eat() - increases the pet's energy by 5 & health by 10
    def eat(self):
        self.energy += 5
        self.health += 10
    
    # play() - increases the pet's health by 5
    def play(self):
        self.health += 5

    # noise() - prints out the pet's sound
    def noise(self):
        print("woof woof")

    def show_pet_instance(self):
        print(self.name)
        print(self.type)
        print(self.health)
        print(self.energy)
        return self

class Dog(Pet):
    def __init__(self, name, type, tricks):
        super().__init__(name, type, tricks)
