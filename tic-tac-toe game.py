class Game:
    board = [" "," "," "," "," "," "," "," "," "]
    play_count = 0
    playables = (1,2,3,4,5,6,7,8,9)
    played_grids = []
    winner_found = False

    @staticmethod
    def grid():
        grid  = (f"\n{Game.board[0]}|{Game.board[1]}|{Game.board[2]}\n-----\n{Game.board[3]}|{Game.board[4]}|{Game.board[5]}\n-----\n{Game.board[6]}|{Game.board[7]}|{Game.board[8]}")
        print(grid)


    def __init__(self,move_type, name):
        self.move_type = move_type
        self.name =  name
        
    
    def make_move(self):
        move = int(input(f"\n{self.name},you are {self.move_type} >>> "))
    
        if move in Game.playables and move not in Game.played_grids:
                Game.board[move -1] = self.move_type # set the move on the board
                Game.play_count += 1 # increment number of plays done by one 
                Game.played_grids.append(move) # add played index to played_grids
        else:
            print("\nEnter a valid grid position")

    @staticmethod
    def winner_checker():
        if Game.board.count[0] == Game.board[1] == Game.board[3]:
            print(f"{Game.board[0]} wins")
            Game.winner_found = True
        else:
            print(f"The current game's play count is {Game.play_count}")
        

player1 = Game(move_type="x", name="playerOne")
player2 = Game(move_type="o", name="playerTwo")


# playloop
def game_instance():
    
    Game.grid()

    for i in str(Game.playables) :
        player1.make_move()
        Game.grid()
        if Game.play_count >= 3:
            Game.winner_checker()
        player2.make_move()
        Game.grid()
        if Game.play_count >= 3:
            Game.winner_checker()
    
    




game_instance()





