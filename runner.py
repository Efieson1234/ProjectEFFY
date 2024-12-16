import random

# Dice roll function with docstring
def roll_dice():
    """Rolls a single die and returns the result (1-6)."""
    return random.randint(1, 6)

# Main game logic with scoring
def main():
    """Main function to run the game with score tracking."""
    score = 0  # Initialize score
    for _ in range(3):  # Play 3 rounds
        roll = roll_dice()
        print(f"You rolled: {roll}")
        score += roll  # Add roll to score
    print(f"Final score: {score}")

main()
