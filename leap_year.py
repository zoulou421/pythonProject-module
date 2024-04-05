# Program testing if a year, entered by the user, is a leap year or not
year = input("Enter a year : ")  # We wait for the user to provide the year they wish to test
year = int(year)  # Risk of error if the user has not entered a number
if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
    print("The year entered is a leap year.")
else:
    print("Sorry!The year entered is not a leap year.")
