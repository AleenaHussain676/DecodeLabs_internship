# Expense Tracker

total = 0

while True:
    expense = float(input("Enter expense amount (0 to stop): "))

    if expense == 0:
        break

    total = total + expense

print("\nTotal Spent:", total)