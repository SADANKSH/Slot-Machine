MAX_LINES = 3
MIN_BET = 1
MAX_BET = 500

def deposit():
    while True:
        amount=input("Please enter the Deposit Amount: $")
        if amount.isdigit():
            amount=int(amount)
            if amount>0:
                break
            else:
                print("Amount must be greater than $0.")
        else:
            print("Please enter a valid number for the amount")

    return amount

def get_lines():
    while True:
        lines = input("Please enter the number of lines you want to  bet on 1-3 : ")
        if lines.isdigit():
            lines = int(lines)
            if 0<lines<=3:
                break
            else:
                print("Lines must be greater than 0 and less than 3.")
        else:
            print("Please enter a valid number for valid number of lines")

    return lines

def get_bets(amount,lines):
    while True:
        betline = input("Please enter the BET Amount for each line: ")
        if betline.isdigit():
            tbet = int(betline)*lines
            bet=int(betline)
            if MIN_BET<=tbet<=int(amount) and MIN_BET<=tbet<=MAX_BET:
                break
            elif tbet>MAX_BET:
                print("BET must be smaller than $500")
            elif tbet>int(amount):
                print(f"You have ${amount} in you wallet.")
            else:
                print("BET must be greater than $1")
        else:
            print("Please enter a valid BET Amount.")

    return tbet,bet

def update_wallet(amount,bet):
    amount=amount-bet
    return amount

def game():
       while True:
        balance=0
        if balance==0:
            balance=deposit()

        while balance>0:
            lines=get_lines()
            bet,betline=get_bets(balance,lines)
            balance = update_wallet(balance, bet, winnings)
            print(f'Your balance is ${balance} and you selected {lines} lines.You have successfully placed a bet of ${bet}')

if __name__=='__main__':  
    game()