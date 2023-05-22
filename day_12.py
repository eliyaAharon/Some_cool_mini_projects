# guess a number game
# Global
import random
rounds = 5


def game(difficult: str):
    global rounds
    if difficult == "easy":
        rounds = rounds + 5
    print(f"You have {rounds} attempts remaining to guess the number")
    random_number = random.randint(1, 100)

    for i in range(rounds):
        guess = int(input("Make a guess: "))
        if guess == random_number:
            print("Tou won the game")
            break
        if random_number > guess:
            print("Too low")
        if random_number < guess:
            print("Too high")


print("Welcome to the Number Guessing Game!\n I'm thinking of a number between 1 and 100")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
game(difficulty)
