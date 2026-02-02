import random

playerScore = 0
computerScore = 0



for _ in range(10):
    pSuit = random.choice(["❤️", "♦️", "♣️", "♠️"])
    pCard = random.choice([2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A'])
    cSuit = random.choice(["❤️", "♦️", "♣️", "♠️"])
    cCard = random.choice([2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A'])
    playerCard = pCard , pSuit
    computerCard = cCard , cSuit
    print("Your card is", playerCard)
    print("Computer card is", computerCard)

    if pCard == cCard:
        print("Draw")


    elif pCard == 2 and cCard in [3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']:
        print("Computer wins!")
        computerScore += 1
    elif pCard == 3 and cCard in [4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']:
        print("Computer wins!")
        computerScore += 1
    elif pCard == 4 and cCard in [5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']:
        print("Computer wins!")
        computerScore += 1
    elif pCard == 5 and cCard in [6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']:
        print("Computer wins!")
        computerScore += 1
    elif pCard == 6 and cCard in [7, 8, 9, 10, 'J', 'Q', 'K', 'A']:
        print("Computer wins!")
        computerScore += 1
    elif pCard == 7 and cCard in [8, 9, 10, 'J', 'Q', 'K', 'A']:
        print("Computer wins!")
        computerScore += 1
    elif pCard == 8 and cCard in [9, 10, 'J', 'Q', 'K', 'A']:
        print("Computer wins!")
        computerScore += 1
    elif pCard == 9 and cCard in [10, 'J', 'Q', 'K', 'A']:
        print("Computer wins!")
        computerScore += 1
    elif pCard == 10 and cCard in ['J', 'Q', 'K', 'A']:
        print("Computer wins!")
        computerScore += 1
    elif pCard == 'J' and cCard in ['Q', 'K', 'A']:
        print("Computer wins!")
        computerScore += 1
    elif pCard == 'Q' and cCard in ['K', 'A']:
        print("Computer wins!")
        computerScore += 1
    elif pCard == 'K' and cCard in ['A']:
        print("Computer wins!")
        computerScore += 1
    else:
        print("Player wins!")
        playerScore += 1

if computerScore > playerScore:
    print("Computer wins Match!")
elif computerScore < playerScore:
    print("Player wins Match!")
else:
    print("Draw")
print("Your Score:" , playerScore)
print("Computer Score:" , computerScore)











