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
                print("Lines must be greater than 0.")
        else:
            print("Please enter a valid number for valid number of lines")

    return lines

def main():
    balance=deposit()
    print(f"You have ${balance} in your wallet.")
    
main()