import random

print("Hand Cricket!!!")
print()

# Toss -> Odd or Even
print("Toss")
while True:
    playerChoice = input("Odd or Even: ")
    if playerChoice.lower().strip() == "odd" or playerChoice.lower().strip() == "even":
        break
    else:
        print(playerChoice + " is a wrong choice buddy.")
playerToss = 0
while True:
    try:
        playerToss = int(input("> "))
    except ValueError:
        print("Invalid input")
    if playerToss < 0 or playerToss > 10:
        print("The number should be from 0 to 10 only")
    else:
        break
computerToss = random.randrange(0, 11)
print(f"You've put: {playerToss}")
print(f"Computer put: {computerToss}")
print()

# Toss -> Winning
toss = -1
if playerChoice.lower().strip() == "odd" and (playerToss + computerToss) % 2 != 0:
    toss = 1
    print("You won the toss!!!")
elif playerChoice.lower().strip() == "even" and (playerToss + computerToss) % 2 == 0:
    toss = 1
    print("You won the toss!!!")
elif playerChoice.lower().strip() == "odd" and (playerToss + computerToss) % 2 == 0:
    toss = 0
    print("Computer won the toss...")
elif playerChoice.lower().strip() == "even" and (playerToss + computerToss) % 2 != 0:
    toss = 0
    print("Computer won the toss...")
else:
    print("You've made an mistake LoL...")

# Toss -> Winner choosing to bat or bowl
player = -1
computer = -1
if toss == 1:
    while True:
        playerChosen = input("Choose to (Batting or Bowling): ")
        if playerChosen.lower().strip() == "batting":
            print("You chose to Bat first...")
            player = 1  # Batting
            computer = 0  # Bowling
            break
        elif playerChosen.lower().strip() == "bowling":
            print("You chose to Bowl first...")
            player = 0  # Bowling
            computer = 1  # Batting
            break
        else:
            print("The options are (Batting or Bowling) only.")
elif toss == 0:
    computerChosen = random.randrange(0, 2)
    if computerChosen == 1:
        player = 0  # Bowling
        computer = 1  # Batting
        print("Computer chose to Bat first...")
    else:
        player = 1  # Batting
        computer = 0  # Bowling
        print("Computer chose to Bowl first...")
else:
    print("You've made an mistake LoL...")

# Play
print("Play!!!")
# Play -> Player bat first
if player == 1:
    playerScore = 0
    target = 0
    playerOut = False
    while True:
        playerPlay = 0
        try:
            while True:
                playerPlay = int(input("Batting> "))
                if playerPlay < 0 or playerPlay > 10:
                    print("The number should from 1 to 10 only...")
                else:
                    break
        except ValueError:
            print("It should be an number from 1 to 10 only...")
        computerPlay = random.randrange(0,11)
        if playerPlay == computerPlay:
            print("Player is out...")
            playerOut = True
            target = playerScore + 1
        elif playerPlay is not computerPlay:
            if playerPlay == 0 and not computerPlay == 0:
                playerScore += computerPlay
            else:
                playerScore += playerPlay
        else:
            print("Very strange...")

        print(f"You've put: {playerPlay}")
        print(f"Computer put: {computerPlay}")
        print(f"Score: {playerScore}")
        if playerOut:
            print(f"Target: {target}")
            print()
            break
        else:
            print()

    print("Computer is Batting...")
    computerOut = False
    computerScore = 0
    draw = False
    while True:
        playerPlay = 0
        try:
            while True:
                playerPlay = int(input("Bowling> "))
                if playerPlay < 0 or playerPlay > 10:
                    print("The number should from 1 to 10 only...")
                else:
                    break
        except ValueError:
            print("It should be an number from 0 to 10 only...")
        computerPlay = random.randrange(0, 11)
        if playerPlay == computerPlay:
            print("Computer is out...")
            computerOut = True
        elif playerPlay is not computerPlay:
            if computerPlay == 0 and not playerPlay == 0:
                computerScore += playerPlay
            else:
                computerScore += computerPlay
        else:
            print("Very strange...")

        print(f"You've put: {playerPlay}")
        print(f"Computer put: {computerPlay}")
        print(f"Score: {computerScore}")
        if computerOut:
            if computerScore == playerScore:
                print("Match draw...\nPlay super over...")
                print()
                draw = True
            else:
                print("Player is the winner!!!")
                break
        elif computerScore >= target:
            print("Computer is the winner!!!")
            break
        else:
            print()

        if draw:
            print("Let's play 1 or 2.")
            print("Best of 3.")
            print()
            count = 1
            playerPoints = 0
            computerPoints = 0
            _1or2PlayerBowl = 0
            while True:
                try:
                    while True:
                        _1or2PlayerBowl = int(input("> "))
                        if _1or2PlayerBowl != 1 and _1or2PlayerBowl != 2:
                            print("Only 1 or 2...")
                        else:
                            break
                except ValueError:
                    print("Only 1 or 2...")
                _1or2ComputerBat = random.randrange(1, 3)
                if count == 3:
                    break
                else:
                    if _1or2PlayerBowl == _1or2ComputerBat:
                        playerPoints += 1
                    else:
                        computerPoints += 1
                count += 1
            if _1or2PlayerBowl > _1or2ComputerBat:
                print("Player is the winner!!!")
                break
            else:
                print("Computer is the winner!!!")
                break
#Play -> Computer bat first
else:
    computerScore = 0
    target = 0
    computerOut = False
    while True:
        playerPlay = 0
        try:
            while True:
                playerPlay = int(input("Bowling> "))
                if playerPlay < 0 or playerPlay > 10:
                    print("The number should from 1 to 10 only...")
                else:
                    break
        except ValueError:
            print("It should be an number from 1 to 10 only...")
        computerPlay = random.randrange(0, 11)
        if playerPlay == computerPlay:
            print("Computer is out...")
            computerOut = True
            target = computerScore + 1
        elif playerPlay is not computerPlay:
            if playerPlay == 0 and not computerPlay == 0:
                computerScore += computerPlay
            else:
                computerScore += playerPlay
        else:
            print("Very strange...")

        print(f"You've put: {playerPlay}")
        print(f"Computer put: {computerPlay}")
        print(f"Score: {computerScore}")
        if computerOut:
            print(f"Target: {target}")
            print()
            break
        else:
            print()

    print("Player is Batting...")
    PlayerOut = False
    playerScore = 0
    draw = False
    while True:
        playerPlay = 0
        try:
            while True:
                playerPlay = int(input("Batting> "))
                if playerPlay < 0 or playerPlay > 10:
                    print("The number should from 1 to 10 only...")
                else:
                    break
        except ValueError:
            print("It should be an number from 0 to 10 only...")
        computerPlay = random.randrange(0, 11)
        if playerPlay == computerPlay:
            print("Player is out...")
            PlayerOut = True
        elif playerPlay is not computerPlay:
            if playerPlay == 0 and not computerPlay == 0:
                playerScore += computerPlay
            else:
                playerScore += playerPlay
        else:
            print("Very strange...")

        print(f"You've put: {playerPlay}")
        print(f"Computer put: {computerPlay}")
        print(f"Score: {playerScore}")
        if PlayerOut:
            if computerScore == playerScore:
                print("Match draw...\nPlay super over...")
                print()
                draw = True
            else:
                print("Computer is the winner!!!")
                break
        elif playerScore >= target:
            print("Player is the winner!!!")
            break
        else:
            print()

        if draw:
            print("Let's play 1 or 2.")
            print("Best of 3.")
            print()
            count = 1
            playerPoints = 0
            computerPoints = 0
            _1or2PlayerBat = 0
            while True:
                try:
                    while True:
                        _1or2PlayerBat = int(input("> "))
                        if _1or2PlayerBat != 1 and _1or2PlayerBat != 2:
                            print("Only 1 or 2...")
                        else:
                            break
                except ValueError:
                    print("Only 1 or 2...")
                _1or2ComputerBowl = random.randrange(1, 3)
                if count == 3:
                    break
                else:
                    if _1or2PlayerBat == _1or2ComputerBowl:
                        computerPoints += 1
                    else:
                        playerPoints += 1
                count += 1
            print(f"Player point is {playerPoints}")
            print(f"Computer point is {computerPoints}")
            if playerPoints > computerPoints:
                print("Player is the winner!!!")
                break
            else:
                print("Computer is the winner!!!")
                break







input("Press ENTER to exit.")