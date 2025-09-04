import random

rock = 1
paper = 2
scissors = 3

moves = (rock, paper, scissors)

reply_options = ('rock', 'paper', 'scissors')


class Game:
    def __init__(self):
        print('Ready to play rock, paper, scissors? \nSelect 1 to play "rock", 2 to play "paper", 3 to play "scissors"')
        
    pass

class Players:
    def __init__(self):
        pass

    def get_move(self):
        move = int(input("Enter your move >>> "))
        return move

class Computer:
    def __init__(self):
        pass

    def get_move(self):
        move = random.choice(moves)
        return move
        




player = Players()
computer =  Computer()

computer_played = False


Game()

while computer_played == False:

    player_move = player.get_move()
     
    move = reply_options[int(player_move) -1]
    print(f"You have played {move}")

    computer_move = computer.get_move()

    move = reply_options[int(computer_move) -1]
    print(f"computer plays {move}")

# When tie happens
    if player_move == computer_move:
        print("Tie, play again")

# When player wins
    elif player_move == rock and computer_move == scissors:
        print("You win")
        computer_played = True
    elif player_move == scissors and computer_move == paper:
        print("You win")
        computer_played = True
    elif player_move == paper and computer_move == rock:
        print("You win")
        computer_played = True
    
# When computer wins
    elif computer_move == rock and player_move == scissors:
        print("Computer wins")
        computer_played = True
    elif computer_move == scissors and player_move == paper:
        print("Computer wins")
        computer_played = True
    elif computer_move == paper and player_move == rock:
        print("Computer wins")
        computer_played = True

        


# rules definition
# rock =1 , paper =2, scissors =3
# Rock beats Scissors, Scissors beats Paper, Paper beats Rock.


