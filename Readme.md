# 🎰 Python Slot Machine Game

A simple command-line slot machine game built in Python that simulates the classic casino experience right in your terminal!

## 👨‍💻 Creator
**Sadanksh Gangrade**

## 📝 Description

This is a text-based slot machine game where players can:
- Deposit money into their virtual wallet
- Choose how many lines to bet on (1-3)
- Place bets on each line
- Spin the slot machine with a 3x3 grid
- Win money based on matching symbols across lines
- Continue playing until they run out of money

## 🎮 How to Play

1. **Deposit Money**: Start by depositing money into your virtual wallet
2. **Choose Lines**: Select how many lines you want to bet on (1-3)
3. **Place Bets**: Enter your bet amount per line
4. **Spin**: Watch the slot machine spin and see if you win!
5. **Collect Winnings**: If you get matching symbols across a line, you win!

## 🎯 Game Rules

### Symbols and Values
- **A**: Appears 2 times, Worth 5x your bet
- **B**: Appears 4 times, Worth 4x your bet 
- **C**: Appears 6 times, Worth 3x your bet
- **D**: Appears 8 times, Worth 2x your bet

### Betting Limits
- Minimum bet: $1
- Maximum bet: $500
- Maximum lines: 3

### Winning Conditions
You win when you get the same symbol across an entire horizontal line that you've bet on.

## 🚀 Getting Started

### Prerequisites
- Python 3.x installed on your system

### Installation & Running

1. Clone this repository:
```bash
git clone <your-repository-url>
cd slot-machine-game
```

2. Run the game:
```bash
python main.py
```

3. Follow the on-screen prompts to play!

## 📁 File Structure

```
slot-machine-game/
│
├── main.py          # Main game file containing all game logic
└── README.md        # This file
```

## 🔧 Game Functions

- `deposit()`: Handles initial money deposit
- `get_lines()`: Gets number of lines player wants to bet on
- `get_bets()`: Handles bet amount input and validation
- `slot_spin()`: Generates random slot machine results
- `print_slot()`: Displays the slot machine grid
- `winning()`: Calculates winnings and winning lines
- `update_wallet()`: Updates player's balance
- `game()`: Main game loop

## 🎲 Game Features

- **Input Validation**: All user inputs are validated to prevent errors
- **Dynamic Betting**: Bet amounts are checked against available balance
- **Multiple Lines**: Players can bet on 1-3 lines simultaneously
- **Fair Randomization**: Uses Python's random module for fair slot generation
- **Continuous Play**: Keep playing until you run out of money
- **Real-time Balance**: Track your winnings and losses

## 🏆 Example Gameplay

```
Please enter the Deposit Amount: $100
Please enter the number of lines you want to bet on 1-3: 2
Please enter the BET Amount for each line: 10

A | B | C
D | D | D
B | A | C

You won $40
You won on lines: 2
Your balance is $120 and you selected 2 lines. You have successfully placed a bet of $20
```

## 🤝 Contributing

Feel free to fork this project and submit pull requests for any improvements!


## 🎯 Future Enhancements

- Add more symbol types
- Implement bonus rounds
- Add sound effects
- Create a GUI version
- Add progressive jackpots
- Implement save/load game state

---

**Have fun and gamble responsibly! 🎰**