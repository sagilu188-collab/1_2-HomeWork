import random

playerWins = 0
computerWins = 0

for i in range(3):

  player = int(input("Choose: 1 ✊ - 2 ✋ - 3 🤘"))

  if player == 1:
    print("✊")
  elif player == 2:
    print("✋")
  elif player == 3:
    print("🤘")
  else:
    print("You Out")
    break

  computer = random.randint(1,3)
  if computer == 1:
    print("✊")
  elif computer == 2:
    print("✋")
  elif computer == 3:
    print("🤘")



  if player == computer:

    continue

  elif player == 1 and computer == 2:
    computerWins += 1
  elif player == 1 and computer == 3:
    playerWins += 1

  elif player == 2 and computer == 1:
    playerWins += 1
  elif player == 2 and computer == 3:
    computerWins += 1

  elif player == 3 and computer == 1:
    computerWins += 1
  elif player == 3 and computer == 2:
    playerWins += 1

if computerWins > playerWins:
    print("Computer wins❌")
    print("Computer:" , computerWins)
    print("Player:" , playerWins)

elif computerWins < playerWins:
    print("Player win! 🏆")
    print("Computer:", computerWins)
    print("Player:", playerWins)
else:
    print("Play Again")
    print("Computer:", computerWins)
    print("Player:", playerWins)






