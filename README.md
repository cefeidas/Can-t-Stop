# Simplified Can't Stop Game

This project is a simplified version of the dice game "Can't Stop". It is designed for players who enjoy strategic and competitive games. The objective is to reach the goal number in three columns before the opponent(s).

## Design of the Workflow

The logic workflow of the game experienced several challenges during the coding process. Initially, I attempted to code the entire game, but soon realized that it was too complex for the given time frame. As a result, I created a simplified version of the workflow. However, after some work, it became apparent that the game, adhering to best practices that advise against asking the player for information the game already has, would play automatically after the first turn, without requiring further input from the player.
The original workflow was a recreation of the full game in all logical steps I could find. Unfortunately, I overwrote this file with the new workflow.
The new workflow was designed as follows:
![Workflow](readme_images/Workflow.jpg)
Ultimately, our game landed somewhere in between the original and the new workflow designs, offering a balanced and engaging gameplay experience for the players. 

## Rules

Please find the complete rules of the original game [here](https://www.ultraboardgames.com/cant-stop/game-rules.php). The rules of my simplified version are:

### Number of Players

The game is set up to allow 2 players only. Players will be prompted to enter their names.

### Objective

The goal of the game is to advance to the uppermost square in a column. Players choose the number they want to play with during their first successful roll, and from then on, they will move one square every time this number shows as a valid combination of their roll.

### Setup

You need to open your Python program running in Heroku in one window, and the worksheet in another. Follow the instructions in the console, and see the changes made on the board. If you accidentally change anything on the original board, you can always copy it from the read-only tab “board_template.” The board would look like this:
![Board](readme_images/Worksheet.JPG)


### Game Play

The (two) players enter their names in the order they decide. The player whose turn it is always rolls all 4 dice at once (this will be simulated on the console). They must form two pairs of dice with the numbers they have rolled. The sums of these two pairs determine the column in which the player must introduce a runner.

#### First turn

Anna rolls [2, 3, 4, 5]. The following combinations are possible:
- 2 + 3 = 5
- 2 + 4 = 6
- 2 + 5 = 7
- 3 + 4 = 7
- 3 + 5 = 8
- 4 + 5 = 9

Anna should choose one of the numbers: 5, 6, 7, 8, 9. The chosen number will have to be found every time she gets a valid combination.

She will then decide whether or not she wants to continue rolling the dice. If she decides not to continue, at the end of the turn, she will advance one square in the chosen number column.

If she decides to continue, she will roll the dice again. If the number she chose at the beginning is not present again in the new roll, she will lose her turn and lose any prior advance made during this turn.

If the number she chose at the beginning is present again in the new roll, her turn will continue, and the two successful rolls will be stored temporarily.

If she decides NOT to continue rolling, any advance she made will be permanently stored. Please note that the more you roll the dice, the higher the risk of losing everything, but the higher the opportunity to score many square movements.

#### Second turn

The second turn is similar to the first one. The main differences are that, if you scored anything in the last turn, you will not choose any number in your first roll. Instead, you will try to score with the number you chose in the previous turn. The other difference is that your token will start in the same square it was at the end of the last scoring turn. If you have not scored anything yet, your second turn will be identical to the first one.

### Winning a Column and Winning the Game

A player wins a column and the game when they reach a specific square. This square varies depending on the target number chosen in the first scoring turn.

The reason this number changes is that some numbers are more likely to appear in a dice combination than others. Players can choose whether they want to take a longer path with a more probable number or a shorter path with a less probable number. The target squares for each chosen number are as follows:
- If you choose 2, you must reach square number 3.
- If you choose 3, you must reach square number 5.
- If you choose 4, you must reach square number 7.
- If you choose 5, you must reach square number 9.
- If you choose 6, you must reach square number 11.
- If you choose 7, you must reach square number 12.
- If you choose 8, you must reach square number 11.
- If you choose 9, you must reach square number 9.
- If you choose 10, you must reach square number 7.
- If you choose 11, you must reach square number 5.
- If you choose 12, you must reach square number 3.

Remember to end your turn after reaching the goal square, or you can still lose all your progress!

## Installation and Setup

The code was uploaded to Heroku, following all the instructions given by Code Institute.
To play you will need to run the Heroku file, and this [worksheet]( https://docs.google.com/spreadsheets/d/1k5kOID_92hpI3Mrk8bwVXBK10h9vurLsw7FtvF5iA6M/edit?usp=sharing).
To edit this worksheet, you need permissions. Only the accounts danmarmon1986@gmail.com and can-t-stop@cant-stop-383216.iam.gserviceaccount.com can edit it. Granting editing permissions to the second address allows the program to make the necessary changes.
To open the file, I gave general access to anyone.

## Rationale for Development

The project aims to create an engaging game that challenges players to think strategically while enjoying competitive gameplay. The simplified version allows for quick learning and understanding of the rules, while still providing depth and complexity.

## Target Audience

The game is suitable for anyone who enjoys strategic and competitive games, and can be played by both experienced and novice players. It can be played individually or in groups.

## Bugs and Solutions

Here is a summary of the most important problems found during the development of the game:

### Issue #1:

The first issue identified was that the program kept asking to try again when there was no valid combination of the four numbers that equaled target_number[0].

#### Solution #1:

To solve this issue, we added a check to see if the target_number[0] was found in all_combinations. The loop would break and print "It seems you ran out of luck" if target_number[0] was not found in all_combinations.

### Issue #2:

The update_sheet() function didn't work well when an empty list was given to it.

#### Solution #2:

We added a condition to handle empty lists in the update_sheet() function. If coordinates = [], the function prints a message indicating that the player didn't score, and the worksheet will not be updated.

### Issue #3:

The did_anybody_win() function returned an error when coordinates showed an empty list: [].

#### Solution #3:
We added a condition to handle empty lists in the did_anybody_win() function. If coordinates = [] or any other value different from winning_coordinates, the function returns False and prints "Nobody won during this turn."
the function returns False and prints "Nobody won during this turn."

### Issue #4:

The first successful roll set should set the first number in the returned list as the target number for the next time the player plays their turn().

#### Solution #4:

We modified the turn() function to return both the result and a boolean value indicating whether the player scored or not. This allowed us to keep track of the target number for each player.

### Issue #5:

The update_sheet() function printed the name of the player even if they did not score in the previous turn. This caused the same name to be printed repeatedly in the same row.

#### Solution #5:

We modified the turn() function to return an empty list [] if the player ran out of luck. The update_sheet() function then used this value to avoid updating the sheet for that player. The target number was still stored for the next player's turn.

## Conclusion

This simplified version of "Can't Stop" offers a fun and engaging gaming experience that challenges players to think strategically. It is accessible to players of all levels and can be quickly set up and played by following the provided instructions. Enjoy the game!
