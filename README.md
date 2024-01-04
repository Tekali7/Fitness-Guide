# Fitness Guide

![Responsitivity example](assets/amiresponsive.PNG)

Deployed link to the project: https://fitness-guide-pp3-15a6dec5a52f.herokuapp.com/

# Purpose of this project

The Fitness Guide is a command-line interface program, with two main features from which the user can choose from. A strength reference for 3 different exercises, or a BMI Calculator. After the user inputs the relevant information like gender, weight and height, the app displays/ calculates the requested information. The user can then choose to continue using the selected feature, change to the other feature or to exit the app.

# Table of contents:

* [User Demographic]()

* [User Experience]()
    * [User stories]()
        * [User Goals]()

* [Features]()
    * [Welcome screen]()
    * [Feature selection]()
    * [Strength Guide]()
    * [BMI Calculator]()
    * [Looping Functionality]()
    * [Reusability]()
    * [Input Validation]()
    * [Future implementations]()

* [Technology]()
    * [Languages]()
    * [Frameworks, Libraries and Programs]()

 * [Wireframe]()

* [Testing]()
    * [Validator Testing]()
    * [Manual Testing]()
        * [Features Testing]()
    * [Fixed Bugs]()

* [Deployment]()
    * [How to Deploy with Heroku]()
    * [How to Fork]()
    * [How to Clone]()

* [Credits]()
    * [Code]()

* [Acknowledgments]()

# User Demographic

The target audience for this fitness app would likely include individuals who are interested in maintaining or improving their physical health and fitness. The user demographic may include:
Fitness enthusiasts, Health-conscious individuals, people monitoring their weight etc.

# User Experience

## User stories

### User goals

- As a user, I want to easily calculate my BMI.

- As a user, I want to quickly see and understand the different ranges of the BMI.

- As a user, I want to get a strength reference tailored to me.

- As a user, I want to get strength references for different exercises compared to the average lifter.

- As a user, I want to easily switch between the Strength Guide and the BMI Calculator for comfortable navigation/use.

# Features

The app consists of one terminal with numerous features which offer the user a pleasant user experience.

## Welcome screen

Upon running the app, users are greeted with a welcome message to the Fitness Guide.<br>
![Welcome screen](assets/welcome-screen.PNG)

## Feature selection

Users are prompted to choose between the Strength Guide and the BMI Calculator. Input validation ensures that only valid options ('strength' or 'bmi') are accepted.<br>
![Selection](assets/selection.PNG)

## Strength Guide

When the user selects the Strength Guide, they are prompted to enter their gender, bodyweight, and choose an exercise (bench, squat, or deadlift). Input validation is implemented for gender, weight, and exercise selection. The app provides average strength references tailored to the users gender, weight, and chosen exercise. The strength references are just an example and shouldn't be taken seriously, as they are just to show the function of the feature. After viewing the strength reference, users have the option to get another strength reference, use the BMI Calculator, or exit. <br>
![Strength Guide](assets/strength-guide.PNG)

## BMI Calculator

When the user selects the BMI Calculator, they are prompted to enter their bodyweight, and height. Input validation is implemented for bodyweight, and height. The app then calculates and displays the users BMI. After viewing the BMI, users have the option to make another BMI calculation, use the Strength Guide, or exit.<br>
![BMI Calculator](assets/bmi-calculator.PNG)

## Looping Functionality

The program is designed to loop, allowing users to make multiple calculations, get multiple strength references or to switch between the Strength Guide and the BMI Calculator without having to restart the app. <br>
![Looping](assets/looping.PNG)

## Reusability

Functions like the strength_guide, bmi_calculator, and calculate_bmi are modular and can be reused, promoting code maintainability.

## Input validation

Robust input validation to ensure accurate user interactions, preventing errors and enhancing the overall user experience.<br>
![Input validation](assets/input-validation.PNG)

## Future implementations

Future implementations for this app are.

- A calorie counter to calculate the daily calorie intake.

- A calorie recommendation based on the users daily activity.

# Technology

## Languages

- Python 3.12

## Frameworks, Libraries and Programs

- IDE: [Visual Studio Code](<https://code.visualstudio.com/>)
- Version Control: [Git](<https://gitforwindows.org/>)
- Repository: [GitHub](<https://github.com/>)
- Validator: [](<>)
- Wireframe: [LucidChart](<>)
- Heroku: [Heroku](<https://heroku.com/>)

# Wireframe

- A flowchart was created before programming started to plan the intended programme flow, as per the attached flowchart.

![Flowchart wireframe](assets/readme-imgs/flowchart-wireframe.PNG)

# Testing

## Validator Testing

The [ Validator]() was used to validate the project.
The validation results are displayed with a snippet of the code to indicate their association with the respective page.

## Manual Testing

### Features Testing

#### Welcome screen

| Test Label | Test Action           | Expected Outcome | Test Outcome |
| ---------- | --------------------- | ---------------- | ------------ |
| Welcome screen | Open app | Welcome the user  | PASS         |

#### Feature selection

| Test Label | Test Action           | Expected Outcome | Test Outcome |
| ---------- | --------------------- | ---------------- | ------------ |
| Feature selection | Input "strength" or "bmi" | Lead to respective features   | PASS         |

#### Strength guide

| Test Label | Test Action           | Expected Outcome | Test Outcome |
| ---------- | --------------------- | ---------------- | ------------ |
| Strength Guide| Input required information | Output strength reference  | PASS              |   

#### BMI Calculator

| Test Label | Test Action           | Expected Outcome | Test Outcome |
| ---------- | --------------------- | ---------------- | ------------ |
| BMI Calculator | Input required information | Output calculated BMI  | PASS         |

#### Looping functionality

| Test Label | Test Action           | Expected Outcome | Test Outcome |
| ---------- | --------------------- | ---------------- | ------------ |
| Looping  | Switch from one feature to the other after usage of current feature or exit app | Start of other feature or exited app  | PASS         |

#### General input validation

| Test Label | Test Action           | Expected Outcome | Test Outcome |
| ---------- | --------------------- | ---------------- | ------------ |
| General input validation| Write incorrect inputs | Repeated request to input correct information with correct input example | PASS              |   

## Fixed Bugs

* Bug: The input delivers an error message when required input was typed with a whitespace infront or after.

* Tried solutions:
1. Used .split() method.
2. Used if statement which doesn't allow whitespaces.

* Working/best solution: Add ".strip()" method to the input functions.

# Deployment

## How to Deploy with Heroku

App deployment is the process of making a program live and accessible on the internet for people to visit.

1. Log in to Heroku.
2. Click "Create new app".
3. Choose app name and select a region.
4. Click "Create app".
5. Navigate to the "Settings" tab.
6. Click "Reveal Config Vars".
7. Add Config Var in Heroku's Settings. The key is PORT and the value is 8000.
8. Scroll down to "Buildpacks".
9. Click "Add Buildpack".
10. First add "Python", click save.
11. Second add "Nodejs", click save.

## How to Fork

Forking allows you to create a copy of the original repository in your own GitHub account. This enables you to make changes to the code without affecting the original code.

1. Log into GitHub.
2. Locate repository and select the repository.
3. Select the "Fork" button near the top-right.
4. You should now have a new copy of the original repository in your own GitHub account.

## How to Clone

Cloning allows you to make an exact copy of a code repository, usually for collaboration or to work on different features independently.

1. Log into GitHub.
2. Locate repository and select the repository.
3. Click the green "<> Code" button.
4. If you want to clone using HTTPS, select the copy button in the HTTPS menu.
5. Open Git Bash.
6. Change the current working directory to the location where you want your cloned directory to be.
7. Type "git clone", and then paste the URL you copied earlier and press "Enter".

# Credits

## Code

- The markdown tables were generated with the help of [Tabletomarkdown](<https://tabletomarkdown.com/convert-spreadsheet-to-markdown>)

- Inspiration for the app idea is from [Strengthlevel](https://strengthlevel.com/strength-standards/bench-press)

- The general structure of an if statement inside a while loop was learned from [Tech with Tim](https://www.youtube.com/watch?v=21FnnGKSRZo)

- The .strip() method was taught to me by my mentor Brian Macharia.

- The code for the  if __name__ == '__main__': ... code block was learned from "mCoding" on YouTube. [mCoding](https://www.youtube.com/watch?v=g_wlZ9IhbTs)

# Acknowledgments

- Mentor support, guidance, and tips to improve my coding skills throughout the project from Brian Macharia.