from random import randint, randrange

secret = str(randint(10000, 99999))
gameState = True

def checkCorrect(guess):
    global secret
    output = []
    for idx in range(0,5):
        if guess[idx] == secret[idx]:
            output.append("🟩")
        elif guess[idx] in secret:
            output.append("🟨")
        else:
            output.append("🟥")
    return output

def gameOver(result):
    return not all(elem == "🟩" for elem in result)

score = 0
    guess = input("Guess a 5 digit number: ")
    if guess.isdigit() and len(str(guess)) == 5:
        result = checkCorrect(str(guess))
        print(f"🟥 = not in number\n🟨 = in number, but wrong position\n🟩 = in number and correct position\nresults: {result}")
        score += 1
        gameState = gameOver(result)          
    else:
        print("Not a valid guess. Please input a number with 5 digits!")
print(f"You won! The number was {guess}.\nYou used {score} guesses")