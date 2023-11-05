import random

options = ("ROCK", "PAPER", "SCISSORS")
flag = "Y"


def get_choices():
    player_choice = str(input("Enter a choice(rock, paper or scissors): ")).upper()
    computer_choice = random.choice(options)

    while player_choice not in options:
        print(f"Please select a valid choice (You typed '{player_choice}')!")
        player_choice = str(input("Enter a choice(rock, paper or scissors): ")).upper()

    choices = {"player": player_choice, "computer": computer_choice}
    return choices


def check_win(player, computer):
    print(f"You chose {player}, computer chose {computer}.")
    if player == computer:
        return f"It's a tie (both typed {player})!"
    elif player == "ROCK":
        if computer == "SCISSORS":
            return "You win!"
        return "You loosed!"
    elif player == "PAPER":
        if computer == "ROCK":
            return "You win!"
        return "You loosed!"
    else:
        if computer == "PAPER":
            return "You win!"
        return "You loosed!"


while flag == "Y":
    choices_result = get_choices()
    result = check_win(choices_result["player"], choices_result["computer"])
    print(result)
    flag = str(input("Wanna continue (y/n)? ")).upper()
    while flag not in ("Y", "N"):
        print(f"Please select a valid value! (you typed '{flag}')!")
        flag = str(input("Wanna continue (y/n)? ")).upper()
