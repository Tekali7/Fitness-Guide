def strength_guide():
    """
    Show the average strength of other lifters of the same gender, weight and age.
    """

    print("Welcome to the Strength Guide!\n")

    gender = str(input("Enter your gender ('m' or 'f'): \n")).lower()
    weight = int(input("Enter your weight in kg: \n"))
    age = int(input("Enter your age: \n"))



def bmi_calculator():
    """
    Calculate the BMI of the user with their gender, weight, height and age.
    [weight (kg) / height (cm) / height (cm)] x 10,000
    """

    print("Welcome to the BMI Calculator!\n")

    gender = str(input("Enter your gender ('m' or 'f'): \n")).lower()
    weight = int(input("Enter your weight in kg: \n"))
    height = int(input("Enter your height in cm: \n"))
    age = int(input("Enter your age: \n"))




def main():
    """
    Run program functions.
    """
    print("Welcome to the Fitness Guide!\n")

    while True:
        user_selection = input("Do you want to use the Strength Guide or the BMI Calculator? (Type 'strength' or 'bmi'): \n").lower()

        if user_selection == "strength":
            strength_guide()
            break
        elif user_selection == "bmi":
            bmi_calculator()
            break
        else:
            print("Invalid input. Enter 'strength' or 'bmi'.\n")

main()