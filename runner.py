import random

# Dice roll function with docstring
def roll_dice():
    return [random.randint(1, 6) for _ in range(3)]

# Function to check if all three dice have the same value (tuple out)
def has_tuple_out(dice):
    return len(set(dice)) == 1

# Function to find dice values that appear exactly twice (fixed dice)
def get_fixed_dice(dice):
    return [num for num in set(dice) if dice.count(num) == 2]

# Function to play a single turn for a player
def play_turn(player):
    print(f"{player}'s turn!")
    dice = roll_dice()  # Initial roll of 3 dice
    print(f"You rolled: {dice}")

    # Check for tuple out on the first roll
    if has_tuple_out(dice):
        print("Tuple Out! No points for this turn.")
        return 0

    # Identify fixed dice (values appearing twice)
    fixed = get_fixed_dice(dice)
    while True:
        print(f"Fixed dice: {fixed}")
        unfixed_dice = [d for d in dice if d not in fixed]  # Dice that can still be rerolled

        # If no dice can be rerolled, end the turn
        if not unfixed_dice:
            print("No dice left to reroll. Ending turn.")
            break

        # Ask the player if they want to reroll the unfixed dice
        choice = input(f"Re-roll the unfixed dice {unfixed_dice}? (yes/no): ").lower()
        if choice != 'yes':
            break

        # Reroll the unfixed dice
        for i in range(3):
            if dice[i] not in fixed:
                dice[i] = random.randint(1, 6)
        print(f"New roll: {dice}")

        # Check if the new roll results in a tuple out
        if has_tuple_out(dice):
            print("Tuple Out! No points for this turn.")
            return 0

        # Update the fixed dice after reroll
        fixed = get_fixed_dice(dice)

    # Calculate the score as the sum of all dice
    score = sum(dice)
    print(f"{player} scored {score} points this turn.")
    return score

# Function to play the full game
def play_game(target_score=30):
    print("Welcome to Tuple Out Dice Game!")
    
    # Ask for the number of players and their names
    players = [input(f"Enter Player {i+1}'s name: ") for i in range(int(input("How many players? ")))]
    scores = {player: 0 for player in players}  # Initialize scores for all players

    # Game loop: continue until one player reaches the target score
    while max(scores.values()) < target_score:
        for player in players:
            print("-" * 20)
            scores[player] += play_turn(player)  # Add turn score to the player's total score
            print(f"Scores: {scores}")
            
            # Check if the player has won
            if scores[player] >= target_score:
                print(f"{player} wins with {scores[player]} points!")
                return

# Start the game
play_game()