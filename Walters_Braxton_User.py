class User():
    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0

    def display_info(self):
        print(self.first_name)
        print(self.last_name)
        print(self.email)
        print(self.age)
        print(self.is_rewards_member)
        print(self.gold_card_points)
        return self
    
    def enroll(self):
        if self.is_rewards_member:
            print(f"{self.first_name} is already a member.")
        else:
            self.gold_card_points += 200
            self.is_rewards_member = True
        return self
    
    def spend_points(self, amount):
        if self.is_rewards_member == True:
            if amount > self.gold_card_points:
                print(f"Sorry you only have {self.gold_card_points} points.")
            else:
                self.gold_card_points -= amount
        else:
            print("You need to sign up first!")
        return self

booby = User("Booby", "Bobberson", "booby.bobberson@gmail.com", "69")
booby.display_info().enroll().spend_points(50).display_info().enroll()

tommy = User("Tommy", "Tommerson", "tom.Tommy@gmail.com", 27)
robby = User("Robby", "Robberson", "rob.robber@gmail.com", 59)
tommy.enroll().spend_points(80).display_info()
robby.display_info().spend_points(40)
