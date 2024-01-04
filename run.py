def strength_guide():
    """
    Show the average strength of other lifters
    of the same gender, weight and age.

    Arguments:
    None, user inputs for gender, weight
    and exercise are obtained interactively
    from the users input.

    Returns:
    None, displays average strength
    references and prompts the user for further actions.
    """
    while True:
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

        # Exercise input validation "squat", "bench" or "deadlift"
        exercise = input("Choose an exercise ('squat', 'bench' or 'deadlift'): \n").lower().strip()

        while exercise not in ["bench", "squat", "deadlift"]:
            print("Invalid input. Enter an exercise ('bench', 'squat' or 'deadlift'): \n")
            exercise = input("Choose an exercise ('squat', 'bench' or 'deadlift'): \n").lower().strip()

        exercise_mapping = get_exercise_mapping(gender, weight)

        print(f"\nAverage strength reference for a {gender} lifter with {weight}kg bodyweight:")

        if weight >= 50 and weight <= 80:
            print(f"{exercise_mapping[exercise]} kg for {exercise}.\n")
        elif weight > 80 and weight <= 120:
            print(f"{exercise_mapping[exercise]} kg for {exercise}.\n")
        else:
            print(f"{exercise_mapping[exercise]} kg for {exercise}.\n")

    # Ask the user if they want to get another strength reference,
    # use the bmi calculator, or exit
        user_choice = input("Do you want to:\n"
                    "1. Get another Strength Reference\n"
                    "2. Use the BMI Calculator\n"
                    "3. Exit\n"
                    "Enter the number corresponding to your choice: ")

        if user_choice == '1':
            # Continue with another strength reference
            continue
        elif user_choice == '2':
            # Use the BMI Calculator
            bmi_calculator()
            break  # Exit the loop after using the bmi calculator
        elif user_choice == '3':
            # Exit the program
            print("Exiting the Strength Guide...\nGoodbye!")
            break
        else:
            print("Invalid choice. Please enter '1', '2', or '3'.\n")


def get_exercise_mapping(gender, weight):
    """
    Retrieves average strength exercise mapping
    based on the users gender and weight.

    Arguments:
        gender: str - Users gender, either 'm' or 'f'.
        weight: int - Users weight in kg, must be between 50 and 140.

    Returns:
        dict: A dictionary representing exercise
        mapping for the users gender and weight.
    """

    exercise_mapping = {
        "m": {
            "light": {
                "squat": 100,
                "bench": 100,
                "deadlift": 100
            },
            "middle": {
                "squat": 100,
                "bench": 100,
                "deadlift": 100
            },
            "heavy": {
                "squat": 100,
                "bench": 100,
                "deadlift": 100
            }
        },
        "f": {
            "light": {
                "squat": 100,
                "bench": 100,
                "deadlift": 100
            },
            "middle": {
                "squat": 100,
                "bench": 100,
                "deadlift": 100
            },
            "heavy": {
                "squat": 100,
                "bench": 100,
                "deadlift": 100
            }
        }
    }

    if gender == "m":
        if weight >= 50 and weight <= 80:
            return exercise_mapping["m"]["light"]

        elif weight > 80 and weight <= 120:
            return exercise_mapping["m"]["middle"]

        else:
            weight > 120 and weight <= 140
            return exercise_mapping["m"]["heavy"]

    if gender == "f":
        if weight >= 50 and weight <= 100:
            return exercise_mapping["f"]["light"]

        elif weight > 100 and weight <= 120:
            return exercise_mapping["f"]["middle"]

        else:
            weight > 120 and weight <= 140
            return exercise_mapping["f"]["heavy"]


def bmi_calculator():
    """
    Calculates the BMI of the user with their weight and height,
    and provides options for further actions.

    Arguments:
    None

    Returns:
    None, displays calculated BMI
    and prompts the user for further actions.
    """
    while True:
        print("Welcome to the BMI Calculator!\n")

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
        
        # Calculate the BMI
        bmi = calculate_bmi(weight, height)

        # Give user their BMI calculation
        print(f"\nYour BMI is: {bmi: .2f}\n")

        # Ask the user if they want to make another calculation, use the strength guide, or exit
        user_choice = input("Do you want to:\n"
                        "1. Make another BMI calculation\n"
                        "2. Use the Strength Guide\n"
                        "3. Exit\n"
                        "Enter the number corresponding to your choice: ")

        if user_choice == '1':
            # Continue with another BMI calculation
            continue
        elif user_choice == '2':
            # Use the Strength Guide
            strength_guide()
            break  # Exit the loop after using the strength guide
        elif user_choice == '3':
            # Exit the program
            print("Exiting the BMI Calculator...\nGoodbye!")
            break
        else:
            print("Invalid choice. Please enter '1', '2', or '3'.\n")


def calculate_bmi(weight_kg, height_cm):
    """
    Calculates the BMI based on
    the users weight and height.
    

    Arguments:
        weight_kg (int): Users weight in kilograms.
        height_cm (int): Users height in centimeters.

    Returns:
        float: Calculated BMI using the formula
        [weight (kg) / height (cm) / height (cm)] x 10000.
    """
    return (weight_kg / height_cm ** 2) * 10000


def main():
    """
    Welcome the user to the Fitness Guide and
    prompt them to choose between the Strength Guide
    or the BMI Calculator. Continues to execute the
    selected functionality until the user exits.

    Arguments:
    None

    Returns:
    None, prints outputs and guides the user
    through the selected program functions.
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

# Start point of the script, calls the main function.
if __name__ == "__main__":
    main()