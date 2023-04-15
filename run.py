# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

import gspread
import random
import itertools
from google.oauth2.service_account import Credentials 

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('Can_t_Stop')
board = SHEET.worksheet('board')
data = board.get_all_values()

def presenting_the_game():
    print('Welcome to Cannot stop, a push your luck game.')

    print('This is a simplified version of the game. If you are interested in the rules of the original game, please visit: ""')

    print('The rules of this project can be found on the Readme File.')

    print("let's get started!")

def naming_the_players():
    P1 = input('Player one, please enter your name. ')
    P2 = input('Player two, please enter your name. ')
    return [P1, P2]

def first_turn(player):
    while True:
        numbers = [random.randint(1, 6) for i in range(4)]
        print(f"{player}, your first roll is: {numbers}")
        while True:
            try:
                dice_choice = int(input("From those four numbers, please choose one combination of two dice summed: "))
            except ValueError as e:
                print(f"Invalid data: {e}, please try again.\n")
                continue

            valid_combination = False
            all_combinations = list(itertools.combinations(numbers, 2))
            for comb in all_combinations:
                if dice_choice == sum(comb):
                    valid_combination = True
                    break

            if not valid_combination:
                print(f"{dice_choice} is not a valid combination of two numbers in the list {numbers}. Please try again.")
            else:
                print(f"{dice_choice} is a valid combination of two numbers in the list {numbers}.")
                break

        target_number = {dice_choice: 1}
        break
    result = [target_number]
    print(f'You chose the number {list(target_number.keys())[0]}. You advanced 1 cell.')
    return result


"""
def following_turns(player):
    while True:
        numbers = [random.randint(1, 6) for i in range(4)]
        print(f"{player}, your first roll is: {numbers}")
        while True:
            try:
                dice_choice = int(input("From those four numbers, please choose one combination of two dice summed: "))
            except ValueError as e:
                print(f"Invalid data: {e}, please try again.\n")
                continue

            valid_combination = False
            all_combinations = list(itertools.combinations(numbers, 2))
            for comb in all_combinations:
                if dice_choice == sum(comb):
                    valid_combination = True
                    break

            if not valid_combination:
                print(f"{dice_choice} is not a valid combination of two numbers in the list {numbers}. Please try again.")
            else:
                print(f"{dice_choice} is a valid combination of two numbers in the list {numbers}.")
                break

        target_number = first_turn(Player)
        if dice_choice == [target_number]:
        
        break
    result = [target_number]
    print(result)
    return result
"""


first_turn('Pepito')