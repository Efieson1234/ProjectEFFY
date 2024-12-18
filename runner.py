import random

def roll_dice():
    # Rolls 3 dice and returns their values
    return [random.randint(1, 6) for _ in range(3)]

def has_tuple_out(dice):
    # Checks if all dice have the same value (Tuple Out)
    return len(set(dice)) == 1

def get_fixed_dice(dice):
    # Finds dice values that appear exactly twice (Fixed Dice)
    return [num for num in set(dice) if dice.count(num) == 2]

def play_turn(player):
    print(f"{player}'s turn!")
    dice = roll_dice()
    print(f"You rolled: {dice}")

    if has_tuple_out(dice):
        print("Tuple Out! No points for this turn.")
        return 0

    fixed = get_fixed_dice(dice)
    while True:
        print(f"Fixed dice: {fixed}")
        unfixed_dice = [d for d in dice if d not in fixed]

        if not unfixed_dice:
            print("No dice left to reroll. Ending turn.")
            break

        reroll = input(f"Re-roll the unfixed dice {unfixed_dice}? (yes/no): ").lower()
        if reroll != 'yes':
            break

        for i in range(3):
            if dice[i] not in fixed:
                dice[i] = random.randint(1, 6)
        print(f"New roll: {dice}")

        if has_tuple_out(dice):
            print("Tuple Out! No points for this turn.")
            return 0
        fixed = get_fixed_dice(dice)

    score = sum(dice)
    print(f"{player} scored {score} points.")
    return score

def play_game(target_score=30):
    players = [input(f"Enter Player {i+1}'s name: ") for i in range(int(input("How many players? ")))]
    scores = {player: 0 for player in players}

    while max(scores.values()) < target_score:
        for player in players:
            print("-" * 20)
            scores[player] += play_turn(player)
            print(f"Scores: {scores}")
            if scores[player] >= target_score:
                print(f"{player} wins with {scores[player]} points!")
                return

play_game()