year = input("Enter a year greater than 0 :")
try:
 year = int(year) # Year conversion
 assert year > 0
except ValueError:
 print("You did not enter a number.")
except AssertionError:
 print("The year entered is less than or equal to 0.")
