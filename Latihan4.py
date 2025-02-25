# Latihan Project 4
import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

random_pick = [rock, paper, scissors]
rps = (random.choice(random_pick))
pick = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

if pick == 0:
    print(rock)
    if rps == rock:
        print("You Draw!")
    elif rps == paper:
        print("You Lose!")
    else:
        print("You Win!")
elif pick == 1:
    print(paper)
    if rps == rock:
        print("You Win!")
    elif rps == paper:
        print("You Draw!")
    else:
        print("You Lose!")
elif pick == 2:
    print(scissors)
    if rps == rock:
        print("You Lose!")
    elif rps == paper:
        print("You Win!")
    else:
        print("You Draw!")
else:
    print("???")

print("Computer Chose:")
print(rps)