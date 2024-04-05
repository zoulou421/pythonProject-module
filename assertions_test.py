year = input("Enter a year greater than 0 :")
try:
    year = int(year)  # Year conversion
    if year <= 0:
        raise ValueError("the year entered is negative or zero")
except ValueError:
    print("You did not enter a number.")
except ValueError:
    print("The value entered is invalid (the year may benegative).")
