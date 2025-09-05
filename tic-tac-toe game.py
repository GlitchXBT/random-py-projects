board = {
    'a': " ",
    'b': " ",
    'c': " ",
    'd': " ",
    'e': " ",
    'f': " ",
    'g': " ",
    'h': " ",
    'i': " "
}


def print_grid():
    grid  = (f"{a}|{b}|{c}\n-----\n{d}|{e}|{f}\n-----\n{g}|{h}|{i}")
    print(grid)


class Players:
    def __init__(self,move_type):
        self.move_type = move_type
        

    def get_move(self):
        move = int(input(">>> "))
        if 0 < move <=9:
            return move
        else:
            print("invalid move")
    


    



player1 = Players(move_type="x")
player2 = Players(move_type="o")

Game_over = False
playables = (1,2,3,4,5,6,7,8,9)
play_count = 0

board[0] = "x"

print_grid()
while Game_over == False:
    print_grid()

    player1_move = player1.get_move()
    if player1_move in playables:
        grid_fields[player1_move -1] = "x"
        print_grid()

        Game_over = True

# a = "x"


