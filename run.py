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
    print('This is a simplified version of the game. If you are interested in the rules of the original game, please visit:')
    print('The rules of this project can be found in the README file.')
    print("Let's get started!")

def naming_the_players():
    P1 = input('Player one, please enter your name: ')
    P2 = input('Player two, please enter your name: ')
    return [P1, P2]

def turn(target_number, player):
    original_target_number = target_number.copy()
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

            if target_number and target_number[0] not in [sum(comb) for comb in all_combinations]:
                print("It seems you ran out of luck")
                print(f"Returning the original value of target_number: {original_target_number}")
                return original_target_number
            elif not valid_combination:
                print(f"{dice_choice} is not a valid combination of two numbers in the list {numbers}. Please try again.")
                continue
            elif not target_number:
                target_number = [dice_choice, 1]
                break
            elif dice_choice == target_number[0]:
                target_number[1] += 1
                break
            else:
                print("This is not your target number.")
                continue

        result = target_number
        print(f'You chose the number {result[0]}. You advanced {result[1]} cell(s).')

        while True:
            continue_rolling = input("Do you want to continue rolling the dice? Y/N: ").upper()
            if continue_rolling == 'Y':
                break
            elif continue_rolling == 'N':
                print(f"Returning the result: {result}")
                return result
            else:
                print("Invalid input. Please enter Y or N.")

def update_sheet(coordinates, player):
    if not coordinates:
        print(f'{player},. You did not score. The worksheet will not be updated.')
        return

    row = coordinates[1] + 2
    col = coordinates[0]
    worksheet_to_update = SHEET.worksheet('board')
    current_value = worksheet_to_update.cell(row, col).value
    new_value = current_value + ", " + player if current_value else player
    worksheet_to_update.update_cell(row, col, new_value)
    print("worksheet updated successfully.")

def did_anybody_win(player, coordinates):
    winning_coordinates = [[2, 3], [3, 5], [4, 7], [5, 9], [6, 11], [7, 13], [8, 11], [9, 9], [10, 7], [11, 5], [12, 3]]
    if coordinates in winning_coordinates:
        print(f'Congratulations {player}!! You won the Game!!')
        return True
    else:
        return False

def main():
    presenting_the_game()
    players = naming_the_players()
    coord_p1 = turn([], players[0])
    update_sheet(coord_p1, players[0])
    coord_p2 = turn([], players[1])
    update_sheet(coord_p2, players[1])
    while not did_anybody_win(coord_p1) and not did_anybody_win(coord_p2):
        coord_p1 = turn(coord_p1, players[0])
        update_sheet(coord_p1, players[0])
        coord_p2 = turn(coord_p2, players[1])
        update_sheet(coord_p2, players[1])


main()