import random


player = int(input("Choose: 1 ✊ - 2 ✋ - 3 🤘"))

if player == 1:
    print("✊")
elif player == 2:
    print("✋")
elif player == 3:
    print("🤘")


computer = random.randint(1,3)
if computer == 1:
    print("✊")
elif computer == 2:
    print("✋")
elif computer == 3:
    print("🤘")



if player == computer:
    print("Draw🤝")

elif player == 1 and computer == 2:
    print("Computer wins❌")
elif player == 1 and computer == 3:
    print("You win🏆")

elif player == 2 and computer == 1:
    print("You win🏆")

elif player == 2 and computer == 3:
    print("Computer wins❌")

elif player == 3 and computer == 1:
    print("Computer wins❌")

elif player == 3 and computer == 2:
    print("You win🏆")