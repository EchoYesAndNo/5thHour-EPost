#Halloween Day
from operator import truediv

truediv = truediv

enter_neighborhood = True or False
say_Trick_or_Treat = True or False

print("You wake up and get ready for trick or treating that starts at 6pm")
print("You have to choose between three costumes")

three_costumes = {
    "scary_costume" : {
    "Type" : "Scary",
    "Accessories" : "Mask",
    "Group costume" : False
    },
    "funny_costume" : {
    "Type" : "Funny",
    "Accessories" : "Wig",
    "Group costume" : False
    },
    "cute_costume" : {
    "Type" : "Cute",
    "Accessories" : "Makeup",
    "Group costume" : True
    }
}

print(three_costumes["scary_costume"]["Type"])
print(three_costumes["funny_costume"]["Type"])
print(three_costumes["cute_costume"]["Type"])

costume_choosing = int(input("Choose a costume: "))
if costume_choosing == 0:
    print("You chose the scary costume")
elif costume_choosing == 1:
    print("You chose the funny costume")
else:
    print("You chose the cute costume")

answer = input("Would you like to continue? (yes/no): ")
cleaned_answer = answer.strip().lower()

if costume_choosing == 0:
    print("You head to the least scariest part of the neighborhood by yourself")
    if enter_neighborhood == True:
        print(answer)
        print(cleaned_answer)
        if cleaned_answer == "yes":
            print("You see all of the Halloween decorations in the neighborhood")
        elif cleaned_answer == "no":
            if say_Trick_or_Treat:
                print(answer)
                print(cleaned_answer)
                if cleaned_answer == "yes":
                    print("You head home and open your bag of candy only to find out it is filled with your favorite candies")
    else:
        print("You go find friends to play with at the Halloween costume contest in the park")
elif costume_choosing == 1:
    print("You head to a part of the neighborhood you know house by house by yourself")
    if enter_neighborhood == True:
        print("You see all of your family walking to you to give you the funniest costume award")
    elif say_Trick_or_Treat == True:
        print("The funny looking parent who is also wearing the same costume as you, wants to take a picture with you")
    else:
        print("You head back to your house with your pajamas on to watch all the Halloween Movies in order")
elif costume_choosing == 2:
    print("You head to the scariest part of the neighborhood with all of your friends wearing Care Bear Costumes")
    if enter_neighborhood == True:
        print("You take videos of you and your friends ding dong ditching")
    elif say_Trick_or_Treat == True:
        print("The door you go to is a scary old man who chases you and your friends out of the neighborhood")
    else:
        print("You hang out with your friends at the Halloween party and takes pictures")












