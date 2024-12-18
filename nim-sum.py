import random

class NimSum:
    def __init__(self):
        self.board = NimSum.make_board() # initial board
        self.player = NimSum.assign_player() # assigns player 
        self.curPlayer = 1

    def play(self):
        while not self._game_end():
            self._draw_game()
            if self.curPlayer == self.player:
                print("your turn!")
                while True:
                    try:
                        player_move_row = int(input("Which row would you like to play? (Enter a number): "))
                        if 1 <= player_move_row <= len(self.board):  # Checking valid row
                            player_move_blocks = int(input("How many blocks do you want to take? "))
                            if 0 < player_move_blocks <= self.board[player_move_row - 1]:  # Checking valid block amount
                                self.board[player_move_row - 1] -= player_move_blocks
                                self._next_player()  # Switch to computer
                                break
                            else:
                                print("Not a valid block amount. Please pick another block!")
                        else:
                            print("Not a valid row. Please try again.")
                    except ValueError:
                        print("Please enter a valid number.")
            else:
                print("computers turn!")
                self._play_game() # computer plays
                self._next_player() # switch to user
        print("Final board state:", self.board)
        if self.curPlayer == self.player:
            print("You won! :)")
        else:
            print("Computer won! :(")

    # determines if the game has ended
    def _game_end(self):
        return sum(self.board) == 0
    
    # draws the game by drawing telling who the current player is and the current board
    def _draw_game(self):
        print(f"{self.curPlayer} now playing...")
        for row in range(len(self.board)):
            print(f"Row {row + 1}: " + ("X" * self.board[row]))

    def _play_game(self):
        max_row = max(self.board)
        max_row_index = self.board.index(max_row)
        # checks if it is given a winningboard
        # if it does plays a random move
        if NimSum.add_nim_bits(self.board) == 0:
            index = random.randint(0, len(self.board) - 1)
            self.board[index] = random.randint(0, self.board[index])
        # if not finds the largest row and subtracts one from it until the board becomes winning
        else:
            for i in range(max_row):
                self.board[max_row_index] -= 1
                if NimSum.add_nim_bits(self.board) == 0:
                    break
                else: 
                    continue

    def _next_player(self):
        if self.curPlayer == 1:
            self.curPlayer = 2
        else:
            self.curPlayer = 1
    
    @staticmethod
    # adds the nim bits to determine which move to make
    def add_nim_bits(board):
        nim_sum = 0
        for row in board:
            nim_sum ^= row
        return nim_sum

    @staticmethod
    # creates the board
    def make_board():
        board = []
        randomrows = random.randint(2,8)
        for x in range(randomrows):
            board.append(random.randint(1,7))
        return board

    @staticmethod
    # asks the user what player they want to be and assigns it
    def assign_player():
        while True:
            player_str = input("Which player? (1/2)")
            if player_str in ['1', '2']:
                player = int(player_str)
                break
            else:
                print("not an option, please enter 1 or 2")
        print(f"playing as player {player}.")
        return player

game = NimSum()
game.play()