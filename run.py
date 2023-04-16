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
    """
    This function prints introductory sentences to help the players understand the game before it starts.
    """
    print("Welcome to Can't stop, a push your luck game.")
    print('This is a simplified version of the game. If you are interested in the original rules, please visit: "https://www.ultraboardgames.com/cant-stop/game-rules.php"')
    print('The rules for this project can be found in the README file.')
    print("Let's get started!")

def naming_the_players():
    """
    "This function asks and stores the names of two players." 
    """
    P1 = input('Player one, please enter your name: ')
    P2 = input('Player Two, please enter your name (choose a name that is different from Player One): ')
    return [P1, P2]

def get_dice_choice(numbers, target_number):
    while True:
        try:
            dice_choice = int(input("From those four numbers, choose any two numbers and add them together, or enter your target number if you already have one: "))
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
            print(f"You pushed your luck too hard and will go back to the starting square for this turn: ({target_number})")
            return None
        elif not valid_combination:
            print(f"{dice_choice} is not the result of adding any two of the rolled dice({numbers}). Please try again.")
            continue
        else:
            return dice_choice


def handle_continue_rolling():
    while True:
        continue_rolling = input("Do you want to continue rolling the dice? Y/N: ").upper()
        if continue_rolling == 'Y':
            return True
        elif continue_rolling == 'N':
            return False
        else:
            print("Invalid input. Please enter Y or N.")


def turn(target_number, player):
    original_target_number = target_number.copy()
    scored = False

    while True:
        numbers = [random.randint(1, 6) for i in range(4)]
        print(f"{player}, you rolled the following numbers: {numbers}")

        dice_choice = get_dice_choice(numbers, target_number)
        if dice_choice is None:
            return original_target_number, False

        if not target_number:
            target_number = [dice_choice, 1]
            scored = True
        elif dice_choice == target_number[0]:
            target_number[1] += 1
            scored = True

        result = target_number
        print(f'You chose the number {result[0]}. You moved up to the row {result[1]}.')

        if not handle_continue_rolling():
            print(f"The result is: {result}")
            return result, scored

def update_sheet(coordinates, player, scored):
    """
    This function updates the worksheet with the values returned from the turn() function. 
    """
    if not coordinates or not scored:
        print(f"{player}, you did not score. The worksheet will not be updated.")
        return

    row = coordinates[1] + 2
    col = coordinates[0]
    worksheet_to_update = SHEET.worksheet('board')
    current_value = worksheet_to_update.cell(row, col).value
    new_value = current_value + ", " + player if current_value else player
    worksheet_to_update.update_cell(row, col, new_value)
    print("Worksheet updated successfully.")

def did_anybody_win(player, coordinates):
    """
    This function checks if any player has won the game using the values from the turn() function.
    """
    if not coordinates:
        print("No one won this turn.")
        return False

    winning_coordinates = [[2, 3], [3, 5], [4, 7], [5, 9], [6, 11], [7, 12], [8, 11], [9, 9], [10, 7], [11, 5], [12, 3]]
    if coordinates in winning_coordinates:
        print(f'Congratulations {player}!! You won the Game!!')
        print("If you feel like playing again, just remember to clear all the values from the worksheet before starting. In the meantime, be proud of your awesome victory; it's now on display for everyone to admire!")
        return True
    else:
        print("Nobody won during this turn.")
        return False

def main():
    presenting_the_game()
    players = naming_the_players()
    target_number_p1 = []
    target_number_p2 = []
    while True:
        result_p1, scored_p1 = turn(target_number_p1, players[0])
        if scored_p1:
            update_sheet(result_p1, players[0])
        target_number_p1 = result_p1

        result_p2, scored_p2 = turn(target_number_p2, players[1])
        if scored_p2:
            update_sheet(result_p2, players[1])
        target_number_p2 = result_p2

        if did_anybody_win(players[0], result_p1) or did_anybody_win(players[1], result_p2):
            break


main()