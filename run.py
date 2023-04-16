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

def roll_dice():
    """
    This function rolls the four dice and returns the resulting numbers.
    """
    return [random.randint(1, 6) for i in range(4)]


def get_dice_combinations(numbers):
    """
    This function returns all the possible combinations of two dice from the rolled numbers.
    """
    return list(itertools.combinations(numbers, 2))


def get_valid_choice(target_number, dice_combinations):
    """
    This function validates the player's choice of dice numbers and returns the chosen number if it's valid.
    """
    while True:
        try:
            dice_choice = int(input("From those four numbers, choose any two numbers and add them together, or enter your target number if you already have one: "))
        except ValueError as e:
            print(f"Invalid data: {e}, please try again.\n")
            continue

        valid_combination = False
        for comb in dice_combinations:
            if dice_choice == sum(comb):
                valid_combination = True
                break

        if target_number and target_number[0] not in [sum(comb) for comb in dice_combinations]:
            print("It seems you ran out of luck")
            print(f"You pushed your luck too hard and will go back to the starting square for this turn: ({target_number})")
            return None
        elif not valid_combination:
            print(f"{dice_choice} is not the result of adding any two of the rolled dice. Please try again.")
            continue
        else:
            return dice_choice


def should_continue_rolling():
    """
    This function asks the player if they want to continue rolling the dice and returns True if they do, False otherwise.
    """
    while True:
        continue_rolling = input("Do you want to continue rolling the dice? Y/N: ").upper()
        if continue_rolling == 'Y':
            return True
        elif continue_rolling == 'N':
            return False
        else:
            print("Invalid input. Please enter Y or N.")


def turn(target_number, player):
    """
    This function handles all actions that occur in each turn of the game.
    """
    original_target_number = target_number.copy()
    scored = False

    while True:
        numbers = roll_dice()
        print(f"{player}, you rolled the following numbers: {numbers}")
        dice_combinations = get_dice_combinations(numbers)
        dice_choice = get_valid_choice(target_number, dice_combinations)

        if dice_choice is None:
            return original_target_number, False
        elif not target_number:
            target_number = [dice_choice, 1]
            scored = True
        elif dice_choice == target_number[0]:
            target_number[1] += 1
            scored = True

        print(f'You chose the number {target_number[0]}. You moved up to the row {target_number[1]}.')

        if not should_continue_rolling():
            print(f"The result is: {target_number}")
            return target_number, scored

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
    """
    This function serves as a control tower and calls all the other functions in the appropriate order.
    """
    presenting_the_game()
    players = naming_the_players()
    target_numbers = [[], []]  # Initialize target numbers for both players

    while True:
        target_number, scored = turn(target_numbers[0], players[0])
        target_numbers[0] = target_number
        update_sheet(target_numbers[0], players[0], scored)
        if did_anybody_win(players[0], target_numbers[0]):
            break

        target_number, scored = turn(target_numbers[1], players[1])
        target_numbers[1] = target_number
        update_sheet(target_numbers[1], players[1], scored)
        if did_anybody_win(players[1], target_numbers[1]):
            break


main()