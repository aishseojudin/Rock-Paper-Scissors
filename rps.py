import random

def play():
    user = input("What's your choice? 'r' for rock, 'p' for paper, 's' for scissors\n")
    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        print (f"You choosed {user} and the computer choosed {computer}")
        return 'It\'s a tie'
    if is_win(user, computer):
        print (f"You choosed {user} and the computer choosed {computer}")
        return 'You won!'
    print (f"You choosed {user} and the computer choosed {computer}")
    return 'You lost!' 

def is_win(player, opponent):
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') \
        or (player == 'p' and opponent == 'r'):
        return True

print(play())