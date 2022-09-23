# rock paper scissors game
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

user_choice = input("Choose rock, paper or scissors: ")
computer_choice = random.choice(["rock", "paper", "scissors"])

if user_choice == 'rock':
    print(rock)
elif user_choice == 'paper':
    print(paper)
else:
    print(scissors)

if computer_choice == 'rock':
    print(f'Computer chose: {rock}')
elif computer_choice == 'paper':
    print(f'Computer chose: {paper}')
else:
    print(f'Computer chose: {scissors}')

if user_choice == computer_choice:
    print('Tie')
elif (user_choice == 'paper' and computer_choice == 'rock') or (user_choice == 'rock' and computer_choice ==
                                                                'scissors') or (user_choice == 'scissors' and
                                                                                computer_choice == 'paper'):
    print('You win')
else:
    print('Computer win')
