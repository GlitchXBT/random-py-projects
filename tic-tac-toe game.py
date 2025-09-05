class Players:
    def __init__(self,move_type, name):
        self.move_type = move_type
        self.name =  name
        

    def get_move(self):
        move = int(input(f"{self.name} >>> "))
        if 0 < move <=9:
            return move
        else:
            print("invalid move")
    

board = [" "," "," "," "," "," "," "," "," "]

player1 = Players(move_type="x", name="playerOne")
player2 = Players(move_type="o", name="playerTwo")

def print_grid():
    grid  = (f"{board[0]}|{board[1]}|{board[2]}\n-----\n{board[3]}|{board[4]}|{board[5]}\n-----\n{board[6]}|{board[7]}|{board[8]}")
    print(grid)

    



Game_over = False
playables = (1,2,3,4,5,6,7,8,9)
play_count = 0

print_grid()

while Game_over == False:

    player1_move = player1.get_move()
    if player1_move in playables:
        board[player1_move -1] = "x"
        play_count += 1
        print_grid()
    else:
        print("Enter a valid grid position")
        
        Game_over = True




