import random

def play():
    print("what's ypur choice?")
    user = input("'r' for rock, 'p' for paper ans 's' for scissors")
    computer = random.choice(['r','p','s'])

    if user == computer:
        return 'tie'

    if is_win(user, computer):
        return 'you won!'

    return 'You lost!'    

def is_win(player, opponent):
    if (player == 'r' and opponent == 'p') or (player == 's' and opponent == 'r') or (player == 'p' and opponent == 's'):
        return True

print(play())