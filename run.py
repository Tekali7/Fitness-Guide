def strength_guide():
    """
    Show the average strength of other lifters of the same gender, weight and age.
    """

    print("Welcome to the Strength Guide!\n")

    # Gender input validation "m" or "f"
    gender = input("Enter your gender ('m' or 'f'): \n").lower().strip()
    
    while gender not in ['m', 'f']:
        print("Invalid input. Enter your gender ('m' or 'f'): \n")
        gender = input("Enter your gender ('m' or 'f'): \n").lower().strip()

    # Weight input validation between 50 and 140
    while True:
        try:
            weight = int(input("Enter your weight in kg (50 - 140): \n").strip())
            if 50 <= weight <= 140:
                break
            else:
                print("Invalid input. Enter a value between 50 and 140.\n")
        except ValueError:
            print("Invalid input. Enter a valid integer for weight.\n")

def bmi_calculator():
    """
    Calculate the BMI of the user with their gender, weight, height and age.
    [weight (kg) / height (cm) / height (cm)] x 10000
    """

    print("Welcome to the BMI Calculator!\n")

    # Gender input validation "m" or "f"
    gender = input("Enter your gender ('m' or 'f'): \n").lower().strip()

    while gender not in ['m', 'f']:
        print("Invalid input. Enter your gender ('m' or 'f'): \n")
        gender = input("Enter your gender ('m' or 'f'): \n").lower().strip()

    # Weight input validation between 50 and 140
    while True:
        try:
            weight = int(input("Enter your weight in kg (50 - 140): \n").strip())
            if 50 <= weight <= 140:
                break
            else:
                print("Invalid input. Enter a value between 50 and 140.\n")
        except ValueError:
            print("Invalid input. Enter a valid integer for weight.\n")

    # Height input validation between 150 and 200
    while True:
        try:
            height = int(input("Enter your height in cm (150 - 200): \n").strip())
            if 150 <= height <= 200:
                break
            else:
                print("Invalid input. Enter a value between 150 and 200.\n")
        except ValueError:
                print("Invalid input. Enter a valid integer for height.\n")

def main():
    """
    Run program functions.
    """
    print("Welcome to the Fitness Guide!\n")

    while True:
        user_selection = input("Do you want to use the Strength Guide or the BMI Calculator? (Type 'strength' or 'bmi'): \n").lower().strip()

        if user_selection == "strength":
            strength_guide()
            break
        elif user_selection == "bmi":
            bmi_calculator()
            break
        else:
            print("Invalid input. Enter 'strength' or 'bmi'.\n")

main()