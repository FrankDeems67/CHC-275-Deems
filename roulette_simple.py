import random

def spin_roulette():
    """Spin the wheel and return the result: 'red', 'black', or 'green'"""
    # 18 red, 18 black, 1 green (simplified)
    outcome = random.choices(['red', 'black', 'green'], weights=[18, 18, 1])[0]
    return outcome

def play_roulette():
    """Play a round of roulette with betting"""
    print("\n=== Simple Roulette ===")
    print("Bet on: red (2-1), black (2-1), or green (36-1)")
    
    # Get bet amount
    while True:
        try:
            bet = int(input("How much do you want to bet? $"))
            if bet <= 0:
                print("Bet must be positive.")
                continue
            break
        except ValueError:
            print("Enter a valid number.")
    
    # Get bet choice
    while True:
        choice = input("Choose red, black, or green: ").strip().lower()
        if choice in ['red', 'black', 'green']:
            break
        print("Invalid choice. Pick red, black, or green.")
    
    # Spin
    result = spin_roulette()
    print(f"Spinning... Result: {result.upper()}")
    
    # Calculate winnings
    if choice == result:
        if result == 'green':
            winnings = bet * 36
        else:
            winnings = bet * 2
        print(f"You win! +${winnings}")
        return winnings
    else:
        print(f"You lose your ${bet}.")
        return -bet

def main():
    balance = 100
    print("Simple Roulette Game")
    print(f"Starting balance: ${balance}\n")
    
    while balance > 0:
        result = play_roulette()
        balance += result
        print(f"Balance: ${balance}")
        
        again = input("Play again? (y/n): ").strip().lower()
        if again != 'y':
            print(f"Final balance: ${balance}. Thanks for playing!")
            break

if __name__ == '__main__':
    main()
