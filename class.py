class Player:
    def __init__(self, name, move_type):
        self.name = name
        self.move_type = move_type

    def get_move(self):
        return int(input(f"\n{self.name}, you are '{self.move_type}' >>> "))


class Board:
    def __init__(self):
        self.board = [" "] * 9
        self.played_grids = []
        self.playables = range(1, 10)
        self.play_count = 0

    def display(self):
        b = self.board
        grid = f"\n{b[0]}|{b[1]}|{b[2]}\n-----\n{b[3]}|{b[4]}|{b[5]}\n-----\n{b[6]}|{b[7]}|{b[8]}\n"
        print(grid)

    def make_move(self, move, move_type):
        if move in self.playables and move not in self.played_grids:
            self.board[move - 1] = move_type
            self.played_grids.append(move)
            self.play_count += 1
            return True
        else:
            print("⚠️: Invalid move.")
            return False

    def is_full(self):
        return self.play_count >= 9


class GameRules:
    @staticmethod
    def check_winner(board):
        b = board.board
        win_conditions = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Rows
            (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Columns
            (0, 4, 8), (2, 4, 6)              # Diagonals
        ]
        for i, j, k in win_conditions:
            if b[i] == b[j] == b[k] != " ":
                print(f"{b[i]} wins! 🎉")
                return True
        return False


class Game:
    def __init__(self, player1, player2):
        self.board = Board()
        self.rules = GameRules()
        self.player1 = player1
        self.player2 = player2
        self.winner_found = False

    def play(self):
        while not self.winner_found:
            for player in (self.player1, self.player2):
                self.board.display()
                move = player.get_move()
                valid = self.board.make_move(move, player.move_type)
                if not valid:
                    continue
                if self.rules.check_winner(self.board):
                    self.winner_found = True
                    self.board.display()
                    return
                if self.board.is_full():
                    print("Tie game!")
                    self.board.display()
                    return


# Run the game
p1 = Player("Alice", "X")
p2 = Player("Bob", "O")
game = Game(p1, p2)
game.play()
