# Get user input for the hour of the day
a = int(input("Enter Hour of the Day: "))

# Determine and print the appropriate greeting
if a < 10:
    print("Good morning")
elif a < 20:
    print("Good day")
else:
    print("Good evening")