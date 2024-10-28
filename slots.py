import random


def spin_row():
    simbol = ['🍒','🍉','🍋','🔔','⭐']

    return [random.choice(simbol) for _ in range(3)]

def print_row(row):
    print('=============')
    print(" | ".join(row))
    print('=============')

def get_payout(row,bet):
    if row[0] == row[1] == row[2]:
        if row[0] == '🍒':
            return bet * 3
        elif row[0] == '🍉':
            return bet * 4
        elif row[0] == '🍋':
            return bet * 5
        elif row[0] == '🔔':
            return bet * 10
        elif row[0] == '⭐':
            return bet * 20
        
    return 0

def main():
    balance = 100

    print('====================================')
    print('Selamat datang di game slot machine ')
    print('Simbol : 🍒 🍉 🍋 🔔 ⭐')
    print('====================================')

    while balance > 0:
        print(f'current balance: ${balance}')

        bet = input('place your bet amount: ')

        if not bet.isdigit():
            print('please enter a valid number')
            continue

        bet = int(bet)

        if bet > balance:
            print('insufficient funds')
            continue

        if bet <= 0:
            print('be mus be greater than 0')
            continue

        balance -= bet

        row = spin_row()
        print('spinning.....\n')
        print_row(row)

        payout = get_payout(row,bet)

        if payout > 0:
            print(f'you won ${payout}')
        else:
            print(f'sorry you lose')

        balance += payout

        play_again = input('do you want to spin again? (Y/N): ')

        if play_again.upper() != 'Y':
            print('==============================')
            print(f'FINAL YOUR BALANCE ${balance}')
            print('==============================')
            break
        
        if balance == 0:
            print('sorry your balance is $0')
            break
        

if __name__ == '__main__':
    main()



--------------------------------------
|  🍒  |  🍉  |  🍋  |  🔔  |  ⭐   |
--------------------------------------