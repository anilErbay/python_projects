#  Guess the Number
#  Number guessing game

import random

guesses_list = []


def start_game():
    attempts = 0
    random_num = random.randint(1, 50)
    print("*******   GUESSING GAME   *******")
    player_name = input("Your name: ")
    wanna_play = input(
        f"Hi {player_name}, would you like to play ? (Yes/No): ")

    if wanna_play.lower() != "yes":
        print("Alright then , see you!")
        exit()

    while wanna_play.lower() == "yes":
        try:
            guess = int(input("Pick a number between 1 and 50: "))
            if (guess < 1 or guess > 50):
                raise ValueError(
                    "Please guess a number within the given range!")
            attempts += 1
            guesses_list.append(guess)

            if guess == random_num:
                print("Well done! You got it!")
                print(f"It took you {attempts} attempts")
                wanna_play = input("Would you like to play again ? (Yes/No): ")
                if wanna_play.lower() != "yes":
                    print("Alright... See you later =)")
                    break
                else:
                    attempts = 0
                    random_num = random.randint(1, 50)
                    continue
            else:
                if guess > random_num:
                    print("It's lower...")
                elif guess < random_num:
                    print("It's higher...")
        except ValueError as e:
            print("Oooppsss..! That's not a valid value. Please try again...")
            print(e)


if __name__ == '__main__':
    start_game()
