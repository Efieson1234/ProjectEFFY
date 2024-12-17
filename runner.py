import random

def roll_dice(num_dice=3):
    """Simulates rolling a given number of dice."""
    return [random.randint(1, 6) for _ in range(num_dice)]

def check_fixed_dice(dice):
    """Checks for fixed dice (two of the same value)."""
    counts = {x: dice.count(x) for x in set(dice)}
    fixed = [num for num, count in counts.items() if count == 2]
    return fixed

def tuple_out(dice):
    """Checks if all three dice have the same value (tupled out)."""
    return len(set(dice)) == 1

def play_turn(player_name):
    """Simulates one turn for a player."""
    print(f"{player_name}'s Turn:")
    dice = roll_dice()
    print(f"Initial Roll: {dice}")

    # Check if tupled out on the first roll
    if tuple_out(dice):
        print("Tuple Out! All dice have the same value. You score 0 points this turn.")
        return 0

    fixed_dice = check_fixed_dice(dice)
    while True:
        print(f"Fixed Dice: {fixed_dice if fixed_dice else 'None'}")
        unfixed_indices = [i for i, die in enumerate(dice) if die not in fixed_dice]

        if not unfixed_indices:  # All dice are fixed
            print("All dice are fixed. Ending turn.")
            break

        unfixed_dice = [dice[i] for i in unfixed_indices]
        reroll = input(f"Do you want to re-roll the unfixed dice {unfixed_dice}? (yes/no): ").strip().lower()
        if reroll != 'yes':
            break

        # Re-roll only the unfixed dice
        for i in unfixed_indices:
            dice[i] = random.randint(1, 6)

        print(f"New Roll: {dice}")

        # Check for tuple out
        if tuple_out(dice):
            print("Tuple Out! All dice have the same value. You score 0 points this turn.")
            return 0

        # Update fixed dice
        fixed_dice = check_fixed_dice(dice)

    score = sum(dice)
    print(f"{player_name} ends their turn with {score} points.")
    return score

def play_game(target_score=30):
    """Simulates the full game until one player reaches the target score."""
    players = []
    num_players = int(input("Enter the number of players: "))
    for i in range(num_players):
        players.append(input(f"Enter Player {i+1}'s name: ").strip())

    scores = {player: 0 for player in players}

    while max(scores.values()) < target_score:
        for player in players:
            print("\n" + "-" * 20)
            scores[player] += play_turn(player)
            print(f"Current Scores: {scores}")
            if scores[player] >= target_score:
                print(f"\nCongratulations {player}! You reached {target_score} points and won the game!")
                return

print("Welcome to the 'Tuple Out' Dice Game!")
