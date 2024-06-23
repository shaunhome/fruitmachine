import random

# Constants
BONUS_SCORE = 20
FIVE_COMBINATION_SCORE = 100
JACKPOT_SCORE = 2000

# Function to calculate the score
def calculate_score(reels):
    if all(num == 5 for num in reels):  # Three fives
        return JACKPOT_SCORE
    elif reels.count(5) == 2:  # Two fives
        return FIVE_COMBINATION_SCORE
    elif all(num == reels[0] for num in reels[:-1]) and reels[0] != 5:  # Three of the same numbers (excluding fives)
        return BONUS_SCORE
    else:
        return 0

# Function to display instructions
def display_instructions():
    print("Welcome to the Fruit Machine Game!")
    print("Instructions:")
    print("1. You will be shown three reels of symbols represented by numbers from 1 to 5.")
    print("2. Scoring:")
    print("   - Any three of the same numbers (excluding fives) will pay a bonus of 20 points.")
    print("   - Any combination of two fives will pay out 100 points.")
    print("   - Three fives pay out the big jackpot of 2000 points.")
    print("3. Your cumulative score will be displayed after each spin.")
    print("4. You will be asked if you wish to make another spin.")

# Main game loop
def fruit_machine_game():
    display_instructions()
    points = 0
    play = input("Do you want to play? (yes/no) ")

    while play.lower() not in ["yes", "no"]:
        print("Please enter 'yes' or 'no'.")
        play = input("Do you want to play? (yes/no) ")

    while play.lower() == "yes":
        randomNumbers = [random.randint(1, 5) for _ in range(3)]
        print(" ".join(map(str, randomNumbers)), end=": ")

        score = calculate_score(randomNumbers)
        points += score

        print("Score =", score)
        print("Total points =", points)

        play = input("Do you want to play again? (yes/no) ")

        while play.lower() not in ["yes", "no"]:
            print("Please enter 'yes' or 'no'.")
            play = input("Do you want to play again? (yes/no) ")

    print("Thank you for playing!")

# Start the game
fruit_machine_game()
