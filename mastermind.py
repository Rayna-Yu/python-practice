from random import randint, randrange

class Mastermind:
    def __init__(self):  
        self.secret = str(randint(10000, 99999)) # generate a random 5 digit number 
        self.gameState = True # game state to be true
        self.score = 0 # set score to be 0

    def play(self):
        while self.gameState:
            guess = input("Guess a 5 digit number: ")
            if guess.isdigit() and len(str(guess)) == 5:
                result = self._check_correct(str(guess))
                print(f"🟥 = not in number\n🟨 = in number, but wrong position\n🟩 = in number and correct position\nresults: {result}")
                self.score += 1
                self.gameState = self._game_over(result)          
            else:
                print("Not a valid guess. Please input a number with 5 digits!")
        print(f"You won! The number was {guess}.\nYou used {self.score} guesses")

    def _check_correct(self, guess):
        output = []
        for idx in range(0,5):
            if guess[idx] == self.secret[idx]:
                output.append("🟩")
            elif guess[idx] in self.secret:
                output.append("🟨")
            else:
                output.append("🟥")
        return output

    def _game_over(self, result):
        return not all(elem == "🟩" for elem in result)
    
m = Mastermind()
m.play()