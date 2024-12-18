import random
import time
import pandas as pd

# Global list to store roll history for analysis
roll_history = []

# Function to roll 3 dice
def roll_dice():
    return [random.randint(1, 6) for _ in range(3)]

# Function to check if all dice have the same value (Tuple Out)
def has_tuple_out(dice):
    return len(set(dice)) == 1

# Function to find dice values that appear exactly twice (Fixed Dice)
def get_fixed_dice(dice):
    return [num for num in set(dice) if dice.count(num) == 2]

# Logs each roll to roll history
def log_roll(player, dice):
    roll_history.append({'Player': player, 'Roll': dice})

# Displays roll statistics at the end of the game
def show_statistics():
    print("\nGame Statistics:")
    df = pd.DataFrame(roll_history)
    print(df.groupby('Player')['Roll'].apply(list))
    print("\nRoll Summary:")
    print(df.groupby('Player')['Roll'].count().reset_index(name='Total Rolls'))

# Function to simulate a player's turn
def play_turn(player):
    print(f"\n{player}'s turn!")
    time.sleep(1)  # Add a short delay for gameplay pacing
    dice = roll_dice()
    log_roll(player, dice)  # Log the initial roll
    print(f"You rolled: {dice}")

    if has_tuple_out(dice):
        print("Tuple Out! No points for this turn.")
        return 0

    fixed = get_fixed_dice(dice)
    while True:
        time.sleep(1)
        print(f"Fixed dice: {fixed}")
        unfixed_dice = [d for d in dice if d not in fixed]

        if not unfixed_dice:
            print("No dice left to reroll. Ending turn.")
            break

        reroll = input(f"Re-roll the unfixed dice {unfixed_dice}? (yes/no): ").lower()
        if reroll != 'yes':
            break

        # Re-roll only the unfixed dice
        for i in range(3):
            if dice[i] not in fixed:
                dice[i] = random.randint(1, 6)
        log_roll(player, dice)  # Log the reroll
        print(f"New roll: {dice}")

        if has_tuple_out(dice):
            print("Tuple Out! No points for this turn.")
            return 0
        fixed = get_fixed_dice(dice)

    score = sum(dice)
    print(f"{player} scored {score} points.")
    return score

# Main game loop
def play_game(target_score=30):
    print("Welcome to Tuple Out Dice Game!")
    players = [input(f"Enter Player {i+1}'s name: ") for i in range(int(input("How many players? ")))]
    scores = {player: 0 for player in players}

    while max(scores.values()) < target_score:
        for player in players:
            print("\n" + "-" * 20)
            scores[player] += play_turn(player)
            print(f"Scores: {scores}")
            if scores[player] >= target_score:
                print(f"\n{player} wins with {scores[player]} points!")
                show_statistics()
                return

# Start the game
play_game()
