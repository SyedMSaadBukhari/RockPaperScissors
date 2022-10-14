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

game = [rock,paper,scissors]
selected = int(input("What do you choose? Type 0 for rock, 1 for paper or 2 for scissors.\n"))
option = game[selected]
print(option)

comp_select = random.randint(0,2)
comp_option = game[comp_select]
print(f"Computer Chose : \n{comp_option}")

if selected >= 3 and selected <0:
    print("Invalid Input")
elif selected ==2 and comp_select == 1:
    print("Yor win")
elif selected ==1 and comp_select ==0:
    print("You win")
elif selected ==0 and comp_select == 2:
    print("You win")
elif selected == comp_select:
    print("Draw")
else:
    print("You lose")

