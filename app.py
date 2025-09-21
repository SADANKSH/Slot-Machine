# Importing Random module to generate the slots.
import random

# Setting Basic Parameters
MAX_LINES = 3
MIN_BET = 1
MAX_BET = 500

# Deciding the Matrix of the  slot Machine
ROWS  = 3
COLS = 3

# Slot Symbols and their Values.
symbol_count={
    'A' : 2,
    'B' : 4,
    'C' : 6,
    'D' : 8
}

symbol_values={
    'A' : 5,
    'B' : 4,
    'C' : 3,
    'D' : 2
}

# Deposit Function
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

# Getting the number of lines to bet on
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

# Getting the  bet amount for each line
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

# Updating the wallet
def update_wallet(amount,bet,winnings):
    if winnings>0:
        amount=amount-bet+winnings
    else:
        amount-=bet
    return amount

# Generating the slots using the Random module imported earlier
def slot_spin(rows,cols,symbols):
    all_symbols = []
    for symbol, symbols_count in symbols.items():
        for _ in range(symbols_count):
            all_symbols.append(symbol)
    columns = []
    for _ in range(cols):
        column =[]
        current_symbols=all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)
    return columns

# Printing the slots as the generated slot was actually not printed
def print_slot(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row],end="")
        print()

# Defining the winning conditions.
def winning(columns , lines , bet, values):
    winnings = 0
    winning_lines =[]
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol]*bet
            winning_lines.append(line + 1)
    return winnings,winning_lines

# Utilizing all the  functions to form the  game and play it.
def game():
       while True:
        balance=0
        if balance==0:
            balance=deposit()

        while balance>0:
            lines=get_lines()
            bet,betline=get_bets(balance,lines)
            slots=slot_spin(ROWS,COLS,symbol_count)
            print_slot(slots)
            winnings, winning_lines = winning(slots,lines,betline,symbol_values)
            balance = update_wallet(balance, bet, winnings)
            print(f"You won ${winnings}")
            print(f"You won on lines : ", *winning_lines)
            print(f'Your balance is ${balance} and you selected {lines} lines.You have successfully placed a bet of ${bet}')

# Adding this to make it runnable as a module in further projects if required.
if __name__=='__main__':
    game()