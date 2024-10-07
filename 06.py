# Get user input for the day number
a = int(input("Enter Day Number of the Week: "))

# Determine the day of the week
if a == 1:
    print("Monday")
elif a == 2:
    print("Tuesday")
elif a == 3:
    print("Wednesday")
elif a == 4:
    print("Thursday")
elif a == 5:
    print("Friday")
elif a == 6:
    print("Saturday")
elif a == 7:
    print("Sunday")
else:
    print("Invalid day number")