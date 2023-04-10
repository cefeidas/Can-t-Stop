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

"""
board = SHEET.worksheet('board')

data = board.get_all_values()

print(data)
"""

print('Welcome to Cannot stop, a push your luck game.')

print('Objective:')

print('The goal of Cannot Stop is to be the first player to reach the top of any three columns on the board.')

print('Setup:')

print('The game board has eleven columns, numbered 2 through 12, and each player chooses three of these columns to be their targets.Each player starts with four markers, and these markers are placed at the bottom of the columns corresponding to their target numbers. Players take turns rolling four dice, and the youngest player goes first.')

print('In this version of the game, the board is drawed on a worksheet, that will be updated as the game flows. The markers will be denoted by Pn, for n being the player number')

print('Gameplay:')

print('On each turn, they roll four dice and try to create one of their target numbers by combining two of the dice. For example, if a player has chosen the columns 4, 8, and 10 as their targets, they might try to create the number 8 by rolling a 3 and a 5. If the player is successful, they can move one of their markers up to the corresponding column on the board. If they fail to create a valid combination, their turn ends and they make no progress. The player can choose to continue rolling the remaining two dice to try and make progress on another target column, but they risk losing all progress on their turn if they fail to make a valid combination with any of the dice. A player can also choose to stop rolling after any roll and advance one of their markers one space in the corresponding column. This is a safe move, but it can be slower than trying to create a valid combination with the remaining dice. If a player reaches the top of a target column, they lock that column and can no longer roll for that target. They can still try to make progress on their remaining targets. If a player fails to make progress on any of their target columns during their turn, they lose all progress and their turn ends. Their opponent then takes their turn. The first player to reach the top of any three columns wins the game.')

print("let's get started!")

P1 = input('Hi players, who is the youngest person in the room? ')

print(f'Great {P1}, you will be player one!')

P2 = input('And who is the second youngest? ')

print(f'Great {P2}, you will be player Two!')

P3 = input("And the remaining one is the oldest. What's your name, oh! old, wise person? ")

def did_anybody_win():
    """
    Checks if the requirements of winning the game are met by any player.
    """ 
    win_or_not = input("Did anybody win? ")
    if win_or_not == 'Y':
        return True
    elif win_or_not == 'N':
        return False

def turn(player):
    """
    Defines all logical steps that take place on each turn
    """
    while True:
        numbers = [random.randint(1, 6) for i in range(4)]
        print(f' {player}, your first roll is: {numbers}')

        while True:
            try:
                dice_choice = [int(x) for x in input('From those four numbers, please choose one or more combinations of two dice summed (separated by a space): ').split()]
            except ValueError as e:
                print(f"invalid data: {e}, please try again.\n")
                continue

            valid_combination = False
            all_combinations = list(itertools.combinations(numbers, 2))

            for choice in dice_choice:
                if choice not in [sum(comb) for comb in all_combinations]:
                    valid_combination = False
                    break
                else:
                    valid_combination = True

            if not valid_combination:
                print(f"{dice_choice} is not a valid combination of two numbers in the list {numbers}. Please, try again.")
            else:
                print(f"{dice_choice} is a valid combination of two numbers in the list {numbers}.")
                break
        break
    checking_turn = input("Can you validly add any of the numbers to your list? Y/N ").upper()
    print("I'll check that in a minute(no offense)")
    want_continue = input("In case you can, do you want to continue rolling the dice? Y/N ").upper()
    result = [dice_choice, checking_turn, want_continue]
    print(result)
    return result

def check_data():
    """
    Check if the answers provided in turn() are correct. Update the list each character chooses in the early stages of the game
    """
    print('Checking data from last turn...')

def update_worksheet():
    """
    Takes the result of each turn and updates the char sheet accordingly.
    """
    print("Updating worksheet...")
    """worksheet_to_update = SHEET.worksheet('board')
    worksheet_to_update.append_cell(row, col, value)
    print(f"{worksheet} worksheet updated successfully.\n")
    """


def who_plays_now():
    """
    checks the lists and decide if any player has won
    """
    print('defining who plays now...')





def main():
    """
    Controls the flow of the game, calling each turn and each worksheet update
    """
    player = [P1]
    while not did_anybody_win():
        turn(player)
        check_data()
        update_worksheet()
        who_plays_now()
    print('Congratulations!! Some person won the game!')

    

main()

