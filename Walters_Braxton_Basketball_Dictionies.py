players = [
    {
    	"name": "Kevin Durant", 
    	"age":34, 
    	"position": "small forward", 
    	"team": "Brooklyn Nets"
    },
    {
    	"name": "Jason Tatum", 
    	"age":24, 
    	"position": "small forward", 
    	"team": "Boston Celtics"
    },
    {
    	"name": "Kyrie Irving", 
    	"age":32,
        "position": "Point Guard", 
    	"team": "Brooklyn Nets"
    },
    {
    	"name": "Damian Lillard", 
    	"age":33,
        "position": "Point Guard", 
    	"team": "Portland Trailblazers"
    },
    {
    	"name": "Joel Embiid", 
    	"age":32,
        "position": "Power Foward", 
    	"team": "Philidelphia 76ers"
    },
    {
        "name": "DeMar DeRozan",
        "age": 32,
        "position": "Shooting Guard",
        "team": "Chicago Bulls"
    }
]

kevin = {
    	"name": "Kevin Durant", 
    	"age":34, 
    	"position": "small forward", 
    	"team": "Brooklyn Nets"
}
jason = {
    	"name": "Jason Tatum", 
    	"age":24, 
    	"position": "small forward", 
    	"team": "Boston Celtics"
}
kyrie = {
    	"name": "Kyrie Irving", 
    	"age":32,
        "position": "Point Guard", 
    	"team": "Brooklyn Nets"
}
    
# Create your Player instances here!
# player_jason = ???




class Player:
    # declaring a new list to append players into it.
    new_team = []
    def __init__(self, indx):
        self.name = indx["name"]
        self.age = indx["age"]
        self.position = indx["position"]
        self.team = indx["team"]
        self.new_team.append(self)

    def show_player_info(self):
        print(self.name)
        print(self.age)
        print(self.position)
        print(self.team)
        return self

    @classmethod
    def print_team_list(cls):
        for player in cls.new_team:
            print(player.name, player.age, player.position, player.team)
            print("-" * 80)

for indx in players:
    Player(indx)

Player.print_team_list()

# kevin_player = Player(kevin)
# kevin_player.show_player_info()
# print("-" * 10)
# jason_player = Player(jason)
# jason_player.show_player_info()
# print("-" * 10)
# kyrie_player = Player(kyrie)
# kyrie_player.show_player_info()

# def som_fun(dict):
#     for i in dict:
#         print(i["name"])
# som_fun(players)

# print(players[0]["name"])


