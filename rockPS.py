import random

def play():
    while True:
        user = input("'r'-> Rock, 'p'-> Paper, and 's'-> Scissors\n")
        Comp = random.choice(['r','p','s'])

        # if they are in tie
        if user == Comp:
            if user == 'r':
                user = Comp = 'Rock'
            if user == 'p':
                user = Comp = 'Paper'
            if user == 's':
                user = Comp = 'Scissors'
            print(f'you choose {user}, computer chooses {Comp}')
            print('tie')
            again = input('Do you want to play again? y/n')
            if again == 'y':
                continue
            else:
                break
        # if player wins
        # r > s, s > p, p > r
        if is_win(user,Comp):
            print('You Won!!')
            again = input('Do you want to play again? y/n')
            if again == 'y':
                continue
            else:
                break

        # If player loses
        if Comp!='r' or 'p' or 's':
            print('You lost! \n Try again')
            again = input('Do you want to play again? y/n')
            if again == 'y':
                continue
            else:
                break
        continue
def is_win(player, opponent):
    # return True if player wins
    # r > s, s > p, p > r
    if(player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent =='r'):
        return True
    
print(play())