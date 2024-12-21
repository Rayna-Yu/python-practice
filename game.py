from mastermind import Mastermind
from nimsum import NimSum

class Game:
    def __init__(self):
        self.people = {}
    
    def login(self):
        while True:
            person = input("Sign in with your name:")
            if person in self.people:
                print(f"Welcome {person}!")
                print(self.people)#????
            else:
                self._add_person(person)
    
    def _add_person(self, person):
        self.people[person] = [0, ] 
        # the information for a person, 1st is games played, second high for nim, third high for mastermind
