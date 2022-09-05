import random
'''
in this game
user make a choice
then computer also make his choice
then the winner is disclosed...
'''

print('Welcome to rock, paper, scissors game')
def make_choices():
    player_choice = input('Enter a choice: (rock, paper, scissors): ')
    options = ['rock', 'paper', 'scissors']
    computer_choice = random.choice(options)
    choices = {'player': player_choice, 'computer': computer_choice}

    return choices

def check_win(player, computer):
    print(f"you choose {player}, computer choose {computer}")
    if player == computer:
        return 'it\'s a tie'
    elif player == 'rock':
        if computer == 'scissors':
            return 'Rock smashes scissors! You win!'  
        else:
            return   'Paper covers rock! You lose.'        
    elif  player == 'paper':
        if computer == 'scissors':
            return 'Scissors cuts paper! You lose.'   
        else:
            return 'Paper covers rock! You win'   
    elif player == 'scissors':
        if computer == 'paper':
            return 'Scissors cuts paper! You win'
        else:
            return 'Rock smashes scissors! You lose'                
    return [player,computer]

choices = make_choices()
result  = check_win(choices['player'], choices['computer'])
print(result)