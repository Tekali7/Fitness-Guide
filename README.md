# Fitness Guide

![Responsitivity example](assets/readme-imgs/am-i-responsive.PNG)

Deployed link to the project: https://fitness-guide-pp3-15a6dec5a52f.herokuapp.com/

# Purpose of this project

The Fitness Guide is a command-line interface program, with two main features from which the user can choose from. A strength reference for 3 different exercises, or a BMI Calculator. After the user inputs the relevant information like gender, weight and height, the app displays/ calculates the requested information. The user can then choose to continue using the selected feature, change to the other feature or to exit the app.

# Table of contents:

* [User Demographic]()

* [User Experience]()
    * [User stories]()
        * [Visitor Goals]()

* [Features]()
    * [Header/Navigation]()
    * [User-Friendly Interface]()
    * [Sound effects]()
    * [Score Counter]()
    * [Game over SweetAlert]()
    * [Instructions Modal]()
    * [Collision Detection]()
    * [Future implementations]()

* [Technology]()
    * [Languages]()
    * [Frameworks, Libraries and Programs]()

 * [Wireframe]()

* [Testing]()
    * [Validator Testing]()
    * [Manual Testing]()
        * [Features Testing]()
        * [Device Testing]()
        * [Browser Compatibility]()
    * [Fixed Bugs]()

* [Deployment]()
    * [How to Deploy with Heroku]()
    * [How to Fork]()
    * [How to Clone]()

* [Credits]()
    * [Code]()

* [Acknowledgments]()

# User Demographic

The game is targeted to a broad audience. Particularly those who enjoy casual and accessible web-based games. With its easy and straightforward controls the game can be played by almost any age group. Also people that are new to gaming have it easy to start with a casual game like JumpJourney.

# User Experience

## User stories

### Visitor goals

- As a visitor, I want to easily understand the main purpose of the website.

- As a visitor, I want to quickly understand the objective of the game.

- As a visitor, I want to be instructed of the controls.

- As a visitor, I want to be able to use more than just one button to control the player.

- As a visitor, I want to see the highest score I managed to get.

# Features

The website consists of one page with numerous features which offer the user a pleasant website experience.

## Header/Navigation

The title of the game is a link that leads back to the start of the page. When clicked, the user can restart the game and refresh their memory of the instructions.
![Header](assets/readme-imgs/header.PNG)

## User-Friendly Interface

The interface of the website is very user-friendly and is designed to provide easy navigation and gameplay. For example: The user can click anywhere on the screen to let the player jump.
![User-Interface](assets/readme-imgs/user-interface.PNG)

## Sound effects

The game provides the player with acoustic feedback when jumping or colliding with the obstacle. This additional feedback increases the experience of the user on the website, as it increases the immersion of the game.
![Sounds](assets/readme-imgs/sounds.PNG)

## Score Counter

The score counter captures the current score that the user managed to play. This encourages the user to replay the game to try and break their recent high-score.
<br>
![Score counter](assets/readme-imgs/score-counter.PNG)

## Game over SweetAlert

The game over SweetAlert function tells the user that the gaming session has ended. Informing them that they collided with the obstacle, thus ending the game. It displays the highest score that the user reached, as well as a "Try Again" button which gives the user the choice to refresh and replay the game.
![Game over alert](assets/readme-imgs/game-over-modal.PNG)

## Instructions Modal

The instructions modal informs the user about the possible ways to control the player, while holding the game on pause. It displays two images with short descriptions underneath each image. The first image displays a left mouse button and the second image displays a arrow up button.
![Instructions Modal](assets/readme-imgs/instructions-modal.PNG)

## Collision Detection

The game checks if the player has collided with an obstacle every 10ms. If a collision occurs the game ends and the score stops counting.
<br>
![Collision Detection](assets/readme-imgs/collision-detection.PNG)

## Future implementations

Future implementations for this website are.

- A pause function to stop the game mid-run.

- Different difficulty setting, from easy to hard.

- Storage of the highest scores, similar to a Top 10 list.

- Online leaderboard to let the user compare themselves to the world.

# Technology

## Languages

- Python 3.12

## Frameworks, Libraries and Programs

- IDE: [Visual Studio Code](<https://code.visualstudio.com/>)
- Version Control: [Git](<https://gitforwindows.org/>)
- Repository: [GitHub](<>)
- Validator: [](<>)
- Wireframe: [LucidChart](<>)

# Wireframe

- Flowchart Wireframe
![Flowchart wireframe](assets/readme-imgs/flowchart-wireframe.PNG)

# Testing

## Validator Testing

The [ Validator]() was used to validate the project.
The validation results are displayed with a snippet of the code to indicate their association with the respective page.

## Manual Testing

### Features Testing

#### Header/Navigation

| Test Label | Test Action           | Expected Outcome | Test Outcome |
| ---------- | --------------------- | ---------------- | ------------ |
| Header     | Click on Header Title | Open Home page   | PASS         |

#### Insctructions modal

| Test Label | Test Action           | Expected Outcome | Test Outcome |
| ---------- | --------------------- | ---------------- | ------------ |
| Instructions modal| Close the modal | Game and score start running   | PASS         |

#### Score counter

| Test Label | Test Action           | Expected Outcome | Test Outcome |
| ---------- | --------------------- | ---------------- | ------------ |
| Score counter| Run game | Count up score  | PASS              |   

#### Collision detection

| Test Label | Test Action           | Expected Outcome | Test Outcome |
| ---------- | --------------------- | ---------------- | ------------ |
| Collision detection | Collide with obstacle | Game and score stop  | PASS         |

#### Game over SweetAlert

| Test Label | Test Action           | Expected Outcome | Test Outcome |
| ---------- | --------------------- | ---------------- | ------------ |
| Game over  | Collide with obstacle | Game over SweetAlert displays   | PASS         |

#### Sound effects

| Test Label | Test Action           | Expected Outcome | Test Outcome |
| ---------- | --------------------- | ---------------- | ------------ |
| Sound effects  | Jump/ Collide | Sound for jump/collision plays   | PASS         |

### Device Testing

Functionality, layout, and responsiveness were tested on the following devices and screens with issues in the collision detection:
This game was optimized for 1920px x 1080px screens.

- Lenovo Monitor 2560px x 1440px
- Samsung Monitor 1920px x 1080px
- Samsung Galaxy S9 1440px x 2960px
- iPhone 11 1792px x 828px

### Browser Compatibility

Testing has been carried out on the following browsers:
- Chrome Version 118.0.5993.117/118
- Safari Version 17.1
- Edge Version 118.0.2088.76
- Firefox Version 119.0

## Fixed Bugs

* Bug:

* Tried solutions:
1. 
2. 
3. 

* Working solution:

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

- The code for the "DOMContentLoaded" eventlistener was learned from the walkthrough project [Love Maths](https://learn.codeinstitute.net/courses/course-v1:CodeInstitute+LM101+2021_T1/courseware/2d651bf3f23e48aeb9b9218871912b2e/234519d86b76411aa181e76a55dabe70/)

- The markdown tables were generated with the help of [Tabletomarkdown](<https://tabletomarkdown.com/convert-spreadsheet-to-markdown>)

- Code for the game idea in general were from [KnifeCircus](https://www.youtube.com/watch?v=bG2BmmYr9NQ)

- Some of the code for the obstacle movement was learned from [java2s](http://www.java2s.com/ref/javascript/javascript-setinterval-move-element.html)

- The code for the instructions modal was learned from [w3schools](https://www.w3schools.com/howto/howto_css_modals.asp)

- The code for the SweetAlert was adapted from [ChatGPT](https://chat.openai.com/)

# Acknowledgments

- Mentor support, guidance, and tips to improve my coding skills throughout the project from Brian Macharia.