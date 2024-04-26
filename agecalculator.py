#---------------------Age Calculator-------------------------------#

def calculate_age():
    print("Welcome to the Age Calculator")

    # Input validation for the username
    while True:
        username = input("Enter your first name: ").strip()
        if username.isalpha():
            break
        else:
            print("Invalid name! Please enter a valid first name.")

    # Input validation for the age
    while True:
        try:
            age = int(input("Please enter your age: ").strip())
            if age >= 0:  # Assuming age cannot be negative
                break
            else:
                print("Invalid age! Please enter a non-negative integer.")
        except ValueError:
            print("Invalid input! Please enter a valid age.")

    # Calculate age based on the selected time unit
    while True:
        unit = input("Please enter a time unit (months/weeks/days): ").strip().lower()
        if unit in ['months', 'weeks', 'days', 'm', 'w', 'd']:
            break
        else:
            print("Invalid unit! Only months/days/weeks are available.")

    # Calculate and display the age
    if unit == 'months' or unit == 'm':
        months = age * 12
        print(f"{username}, your age is approximately {months} months.")
    elif unit == 'weeks' or unit == 'w':
        weeks = age * 52  # Assuming 52 weeks in a year
        print(f"{username}, your age is approximately {weeks} weeks.")
    elif unit == 'days' or unit == 'd':
        days = age * 365  # Assuming 365 days in a year
        print(f"{username}, your age is approximately {days} days.")

if __name__ == "__main__":
    calculate_age()
