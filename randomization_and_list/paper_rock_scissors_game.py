# Rock
import random

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

# Paper
paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

# Scissors
scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

options = [rock, paper, scissors]

my_choice = options[int(input("1 - Pedra, 2 - Papel, 3 - Tesoura? ")) - 1]

computer_choice = options[random.randint(0, 2)]

print(f"Minha escolha é:\n {my_choice}")
print(f"A escolha do computador é:\n {computer_choice}")

if my_choice == computer_choice:
    print("Empate! Tente novamente.")
else:
    if my_choice == options[0] and computer_choice == options[1]:
        print("Você perdeu!")
    elif my_choice == options[0] and computer_choice == options[2]:
        print("Você Venceu!")
    elif my_choice == options[1] and computer_choice == options[2]:
        print("Você venceu!")
    elif my_choice == options[1] and computer_choice == options[2]:
        print("Você perdeu!!")
    elif my_choice == options[2] and computer_choice == options[0]:
        print("Você perdeu!")
    elif my_choice == options[2] and computer_choice == options[1]:
        print("Você venceu")

print("\nFim!")

