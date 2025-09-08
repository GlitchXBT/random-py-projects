class Game:
    board = [" "," "," "," "," "," "," "," "," "]
    play_count = 0
    playables = (1,2,3,4,5,6,7,8,9)
    played_grids = []

    @staticmethod
    def grid():
        grid  = (f"\n{Game.board[0]}|{Game.board[1]}|{Game.board[2]}\n-----\n{Game.board[3]}|{Game.board[4]}|{Game.board[5]}\n-----\n{Game.board[6]}|{Game.board[7]}|{Game.board[8]}\n")
        print(grid)


    def __init__(self,move_type, name):
        self.move_type = move_type
        self.name =  name
        
    
    def make_move(self):
        move = int(input(f"\n{self.name}, you are {self.move_type} >>> "))
    
        if move in Game.playables and move not in Game.played_grids:
                Game.board[move -1] = self.move_type # set the move on the board
                Game.play_count += 1 # increment number of plays done by one 
                Game.played_grids.append(move) # add played index to played_grids
        
        else:
            print("\n⚠️ Enter a valid grid position")

    winner_found = False

    @staticmethod
    def winner_checker():
        empty_grid = " "
        # horizontal grid check
        if Game.board[0] == Game.board[1] == Game.board[2] != empty_grid:
            print(f"{Game.board[0]} wins (horizontal checkmate)🎉 ")
            Game.winner_found = True
        elif Game.board[3] == Game.board[4] == Game.board[5] != empty_grid:
            print(f"{Game.board[3]} wins (horizontal checkmate)🎉 ")
            Game.winner_found = True
        elif Game.board[6] == Game.board[7] == Game.board[8] != empty_grid:
            print(f"{Game.board[6]} wins (horizontal checkmate)🎉 ")
            Game.winner_found = True

        # vertical grid check
        elif Game.board[0] == Game.board[3] == Game.board[6] != empty_grid:
            print(f"{Game.board[0]} wins (vertical checkmate)🎉 ")
            Game.winner_found = True
        elif Game.board[1] == Game.board[4] == Game.board[7] != empty_grid:
            print(f"{Game.board[1]} wins (vertical checkmate)🎉 ")
            Game.winner_found = True
        elif Game.board[2] == Game.board[5] == Game.board[8] != empty_grid:
            print(f"{Game.board[2]} wins (vertical checkmate)🎉 ")
            Game.winner_found = True

        # diagonal grid check
        elif Game.board[0] == Game.board[4] == Game.board[8] != empty_grid:
            print(f"{Game.board[0]} wins (diagonal checkmate)🎉 ")
            Game.winner_found = True
        elif Game.board[6] == Game.board[4] == Game.board[2] != empty_grid:
            print(f"{Game.board[0]} wins (diagonal checkmate)🎉 ")
            Game.winner_found = True
        else:
            print(f"\nTotal moves played: {Game.play_count}")
        
# Object creation
player1 = Game(move_type="x", name="playerOne")
player2 = Game(move_type="o", name="playerTwo")


# playloop
def game_instance():
    

    while Game.winner_found == False:
        Game.grid()
    
        player1.make_move()
        Game.grid()
        Game.winner_checker()

        if Game.winner_found == True:
            break
        if Game.play_count >= 9:
            print("Tie")
            break

        player2.make_move()
        Game.winner_checker()

        if Game.winner_found == True:
            break
        if Game.play_count >= 9:
            print("Tie")
            break
    

game_instance()





