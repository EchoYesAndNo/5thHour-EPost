#Name: Echo Post
#Class: 5th Hour
#Assignment: Scenario 1

#Scenario 1:
#You are a programmer for a fledgling game developer. Your team lead has asked you
#to create a nested dictionary containing five enemy creatures (and their properties)
#for combat testing. Additionally, the testers are asking for a way to input changes
#to the enemy's damage values for balancing, as well as having it print those changes
#to confirm they went through.

#Other than damage which is required, it is up to you to decide what properties are
#important and the theme of the game.

enemy_creatures_dict = {
    "enemy_1" : {
        "Name" : "Godzilla",
        "Strength" : [100000, 200000],
        "Damage" : [1000000, 2000000, 3000000],
        "Ability" : "Radioactive Lazer beam from mouth",
        "Trick" : "Can use radioactivity as a healing method"
    },
    "enemy_2" : {
        "Name" : "Pluto",
        "Strength" : [5, 100],
        "Damage" : 10000,
        "Ability" : "Eats everything",
        "Trick" : "Can roll around that heals him"
    },
    "enemy_3" : {
        "Name" : "Hercules",
        "Strength" : 1000000000000,
        "Damage" : 5000000,
        "Ability" : "Has sword and is very strong",
        "Trick" : "Can throw lightnening bolts as defense mechanism"
    },
    "enemy_4" : {
        "Name" : "Dragon",
        "Strength" : 898700000,
        "Damage" : 1000000,
        "Ability" : "Radioactive Lazer beam from mouth",
        "Trick" : "Can blow deadly fire from mouth"
    },
    "enemy_5": {
        "Name": "Hello Kitty",
        "Strength": 9999999999,
        "Damage": 99999999999999,
        "Ability": "Is immortal, technically",
        "Trick" : "Her bow can be used as a barrier around herself and others, protective bow"
    },
}
print(enemy_creatures_dict)
enemy_creatures_dict["enemy_5"].update({"Damage" : 5000000000})
print(enemy_creatures_dict["enemy_5"])