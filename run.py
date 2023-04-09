# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

import gspread
import random
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

def turn(player):
    while True:
        numbers = [random.randint(1, 6) for i in range(4)]
        print(f' {player}, your first roll is: {numbers}')
        dice_choice = int(input('From those four numbers, please chose one or two combinations of two dice summed: '))
        valid_sum = False
        for i in range(len(numbers)):
            for j in range(i+1, len(numbers)):
                if numbers[i] + numbers[j] == dice_choice:
                    valid_sum = True
                    break
            if valid_sum:
                break

        if valid_sum:
            print(f"{dice_choice} is a valid sum of two numbers in the list {numbers}. The worksheet has been updated")
        else:
           print(f"{dice_choice} is not a valid sum of two numbers in the list {numbers}. Please, try again")

def update_worksheet(row, col, value):
    """
    Receives a list of integers to be inserted into a worksheet 
    Update the relevant worksheet with the data provided
    """
    print(f"Updating {worksheet} worksheet...\n")
    worksheet_to_update = SHEET.worksheet('board')
    worksheet_to_update.append_cell(row, col, value)
    print(f"{worksheet} worksheet updated successfully.\n")

turn(P1)

