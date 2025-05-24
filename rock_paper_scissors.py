## Rock, Paper, Scissors Game
import random

elem = ['Rock', 'Paper', 'Scissors']

while True:
    index = random.randint(0, 2)
    the_chosen_one = elem[index]

    user_input = input("Play your move (rock, paper, scissors): ").lower()

    if user_input.startswith("r"):
        user_choice = "Rock"
    elif user_input.startswith("p"):
        user_choice = "Paper"
    elif user_input.startswith("s"):
        user_choice = "Scissors"
    else:
        print("Invalid input! Please enter rock, paper, or scissors.")
        continue

    print(f"Computer chose: {the_chosen_one}")
    print(f"You chose: {user_choice}")

    if the_chosen_one == user_choice:
        print("It is a Tie!")
    elif (user_choice == "Rock" and the_chosen_one == "Scissors") or \
         (user_choice == "Paper" and the_chosen_one == "Rock") or \
         (user_choice == "Scissors" and the_chosen_one == "Paper"):
        print("You Win!")
    else:
        print("You Lose!")

    # Play again?
    answer = input("Do you want to play again? (y/n): ").lower()
    if answer != 'y':
        print("Thanks for playing!")
        break
