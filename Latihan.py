# Latihan 1
print("1. Mix 500g of Flour, 10g Yeast and 300ml Water in a bowl.")
print("2. Knead the dough for 10 minutes.")
print("3. Add 3g of Salt.")
print("4. Leave to rise for 2 hours.")
print("5. Bake at 200 degrees C for 30 minutes.")

# Latihan 2
print("Notes from Day 1")
print("The print statement is used to output strings")
print("Strings are strings of characters")
print("String Concatenation is done with the + sign")
print("New lines can be created with a \ and the letter n")

# Latihan 3
glass1 = "milk"
glass2 = "juice"

glass = glass1
glass1 = glass2
glass2 = glass
# glass1,glass2 = glass2,glass1

# Latihan Project 1
print("Welcome to the Band Name Generator.")
city = input("What's the name of the city you grew up in? \n\t")
pet = input("What's your pet's name? \n\t")
print("Your band name could be " + city + " " + pet)

# Latihan 4
height = 1.65
weight = 84
bmi = weight / (height ** 2)
print(bmi)

# Latihan Project 2
print("Welcome to the tip calculator!")
total = input("What was the total bill? $")
tip = input("How much tip would you like to give? 10, 12, or 15?\t")
split = input("How many people to split the bill?\t")
pay = (float(total)*(float(tip)/100) + float(total)) / int(split)
print(f"Each person should pay: ${round(pay, 2)}")

# Latihan 5
weight = 85
height = 1.85
bmi = weight / (height ** 2)

# Latihan Project 3
print(r'''
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
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
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
print("You're at a cross road. Where do you want to go?\t")
direction = input('type "left" or "right"\t')
if direction == "right":
    print("Fall into a hole.\tGame Over.")
elif direction == "left":

    print("You've come to a lake. There is and island in the middle of the lake.")
    moment = input('Type "wait" to wait for a boat. Type "swim" to swim across.\t')
    if moment == "swim":
        print("You Attacked by trout.\tGame Over.")
    elif moment == "wait":

        print("You arrive at the island unharmed. There is a house with 3 doors.")
        doors = input("One red, One yellow and One blue. Which colour do you choose?")
        if doors == "red":
            print("You Burned by Fire.\tGame Over.")
        elif doors == "blue":
            print("Eaten by beasts.\tGame Over.")
        elif doors == "yellow":
            print("!!!CONGRATULATIONS YOU WIN!!!")
        else:
            print("Game Over")

print("Refresh to Retry Again LOL")