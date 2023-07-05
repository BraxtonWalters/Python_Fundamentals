import Ninja
import Pets
braxton = Ninja.Ninja("Braxton", "Walters", "Nudges", "Victor", "Jade", "Dog", "fetch")

braxton.feed().walk().bathe()
braxton.pet.show_pet_instance()

print(Ninja.Ninja.__doc__) # why do I have to do this? The double ninja thing.