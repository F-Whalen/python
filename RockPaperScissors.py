#winner = "Tie"

def main ():
    #global winner
    play_game()
    #print ("Game winner is: ", winner)

    

def play_game():
    import random
    computer_number = random.randint(1,3)
    #
    print(computer_number)
    #
    computer_word = turn_to_word(computer_number)
    player_word = get_player_word()
    print('Player picked: ', player_word)
    print("Computer picked: ", computer_word)
    game_winner = compare_words(computer_word, player_word)
    #return game_winner
    print ("Game winner is: ", game_winner)
   


def turn_to_word(c_pick):
    if c_pick == 1:
        return 'rock'
    elif c_pick == 2:
        return 'paper'
    else:
        return 'scissors'


def get_player_word():
    word = input('Enter rock, paper, or scissors: ')
    return word


def compare_words(c_word, p_word):
    if c_word == p_word:
        #winner = "Tie"
        print('Game is a tie.  Play again. ')
        play_game()
    elif c_word == 'rock':
        if p_word == 'paper':
           winner = "Player"
        else:
            winner = "Computer"
    elif c_word == 'paper':
        if p_word == 'rock':
            winner = 'Computer'
        else:
            winner = 'Player'
    elif c_word == 'scissors':
        if p_word == 'rock':
            winner = 'Player'
        else:
            winner = 'Computer'
    return winner
            
# 1 is rock
# 2 is paper
# 3 is scissors

main()
