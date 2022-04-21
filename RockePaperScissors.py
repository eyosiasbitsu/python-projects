import random

def play():
    user = input("'r' fro rock, 'p' for paper, 's' for scissors")
    computer = random.choice(['r','p','s'])

    if user == computer:
        return 'It \'s a tie'
    # rock beats scissors, scissors beats paper, paper beats rock
    
    if wins(user,computer):
        return "Congrats! the user wins"

    return "The user Looses"

def wins(player,opponent):
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True
    return False

print (play())