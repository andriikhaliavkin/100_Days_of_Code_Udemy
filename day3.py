print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
road_choose = input("You're at a cross road. Where do you want to go? type \"left\" or \"right\": ")
if road_choose == "left":
    wait_or_swim_choose = input("You come to a lake. There is an island in the middle of the lake. Type \"wait\" to "
                                "wait for a boat. Type \"swim\" wo swim across: ")
    if wait_or_swim_choose == "wait":
        door_choose = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow "
                            "and one blue. Ehich colour do you choose?: ")
        if door_choose == "yellow":
            print("You opened the yellow door and found a treasure. Congratulations ")
        elif door_choose == "blue":
            print("You opened the blue door. The crocodile beat You")
        else:
            print("You opened red door. Nothing was happened")
    else:
        print("You started to swim. BUt there were sharks in the lake. You were delicious meal for them")
else:
    print("You were met by enemies. It was brave fight but You were killed and robbed")