# Anthony Garcia-Fernandez
# P3LAB_GarciaFernandezAnthony
# This program calculates the most efficient number of dollars, quarters, dimes, nickels, and pennies needed to make up a given amount of money.

# Get the input from the user
money = float(input("Enter a monetary amount: "))

# Convert the money to cents to avoid dealing with floats
cents = int(money * 100)

# Calculate the number of dollars
dollars = cents // 100
cents = cents % 100

# Calculate the number of quarters
quarters = cents // 25
cents = cents % 25

# Calculate the number of dimes
dimes = cents // 10
cents = cents % 10

# Calculate the number of nickels
nickels = cents // 5
cents = cents % 5

# The remaining cents will be the number of pennies
pennies = cents

# Output results
if dollars > 0:
    print(f"{dollars} dollar{'s' if dollars > 1 else ''}")
if quarters > 0:
    print(f"{quarters} quarter{'s' if quarters > 1 else ''}")
if dimes > 0:
    print(f"{dimes} dime{'s' if dimes > 1 else ''}")
if nickels > 0:
    print(f"{nickels} nickel{'s' if nickels > 1 else ''}")
if pennies > 0:
    print(f"{pennies} penn{'y' if pennies == 1 else 'ies'}")
