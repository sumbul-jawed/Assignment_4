import random

def roll_dice():
    # Simulate rolling two dice
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    
    # Calculate total
    total = die1 + die2
    
    # Print the result of each die and the total
    print(f"Die 1: {die1}, Die 2: {die2}, Total: {total}")

def main():
    roll_dice()

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()

