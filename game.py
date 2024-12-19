from mastermind import Mastermind
from nimsum import NimSum

class Game:
    def __init__(self):
        self.people = set()
    
    def login(self):
        while True:
            person = input("Sign in with your name:")
            if person in self.people:
                print(f"Do you want to continue as {person}")
                print(f"Welcome {person}!")
                print(self.people)
            else:
                self._add_person()

class People:
    def __init__(self):
        self.gamesPlayed = 0
        self.high_nimsum_score = 0
        self.high_mastermind_score = 0
    
    def __str__(self):
        print(f"Games player: {self.gamesPlayed}")
        print(f"High score for nimsum: {self.high_nimsum_score}")
        print(f"High score for mastermind: {self.high_mastermind_score}")
