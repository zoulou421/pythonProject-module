# This file houses the code of the Casino, an adapted roulette game

import os
from random import randrange
from math import ceil

# Declaration of starting variables
money = 1000 # We have $1000 at the start of the game

continue_part = True # Boolean which is true as long as we must continue the game
print("You sit at the roulette table with", money,
"$.")

while continue_part: # As long as we have to continue the game we ask the
 #user to enter the number on which they are going to bet
 bet_number = -1
 while bet_number < 0 or bet_number >49:
  bet_number = input("Type the number you want to bet (between 0 and 49) ")
  # We convert the number bet
  try:
    bet_number = int(bet_number)
  except ValueError:
    print("You did not enter a number")
    bet_number = -1
  continue
  if bet_number < 0:
     print("This number is negative")
  if bet_number > 49:
     print("This number is greater than 49")
# Now, we select the amount to bet on the number
abet = 0
while abet <= 0 or abet > money:
 abet = input("Enter your bet amount : ")
 # We convert the stake
 try:
  abet = int(abet)
 except ValueError:
  print("You did not enter a number")
  abet = -1
  continue
  if abet <= 0:
   print("The stake entered is negative or zero.")
  if abet > money:
   print("You can only bet that much, you only have",money, "$")
   #The number bet and the bet have been selected by the user, the roulette is rotated
   number_winning = randrange(50)
   print("The roulette wheel spins... ...and stops on the number",number_winning)
   #We establish the player's gain
  if number_winning == bet_number:
   print("Congratulations ! You obtain", abet * 3, "$ !")
   argent += mise * 3
  elif number_winning % 2 == bet_number % 2: # they are the same color
   abet = ceil(mise * 0.5)
   print("You chose the right color. You obtain",abet, "$")
   money += abet
  else:
   print("Sorry friend, it's not this time. You lose your stake.")
   money -= abet
  # The game is interrupted if the player is ruined
  if money <= 0:
   print("You are ruined! It's the end of the game.")
   continue_part = False
  else:
  #We display the player's money
   print("You now have", money, "$")
  quit_casino = input("Would you like to leave the casino (y/n)? ")
  if quit_casino == "o" or quit_casino == "O":
   print("You leave the casino with your winnings.")
   continue_part = False
   #We pause the system (Windows)
os.system("pause")