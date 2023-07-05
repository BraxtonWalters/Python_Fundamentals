import Pets

class Ninja:
    """
    This is how you init a ninja
    first_name , last_name , treats , pet_food , pet
    """

    # implement __init__( first_name , last_name , treats , pet_food , pet )
    def __init__(self, first_name, last_name, treats, pet_food, pet_name, pet_type, pet_tricks ):
        self.first_name = first_name
        self.last_name = last_name
        self.treats = treats
        self.pet_food = pet_food
        self.pet = Pets.Dog(pet_name, pet_type, pet_tricks)

    # implement the following methods:
    # walk() - walks the ninja's pet invoking the pet play() method
    def walk(self):
        self.pet.play()
        return self

    # feed() - feeds the ninja's pet invoking the pet eat() method
    def feed(self):
        self.pet.eat()
        return self

    # bathe() - cleans the ninja's pet invoking the pet noise() method
    def bathe(self):
        self.pet.noise()
        return self

    def show_instance(self):
        print(self.first_name)
        print(self.last_name)
        print(self.treats)
        print(self.pet_food)
        print(self.pet.name)
        return self