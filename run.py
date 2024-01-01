
def main():
    """
    Run all program functions.
    """
    print("Welcome to the Fitness Guide!\n")

    while True:
        user_selection = input("Do you want to use the Strength Guide or the BMI Calculator? (Type 'strength' or 'bmi'):\n").lower()

        if user_selection == "strength":
            strength_guide()
            break
        elif user_selection == "bmi":
            bmi_calculator()
            break
        else:
            print("Invalid input. Enter 'strength' or 'bmi'.\n")

main()