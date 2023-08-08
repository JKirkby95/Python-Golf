# Python Golf

![am i responsive photo](assets/images/python-golf-ami.png)

Python Golf is a terminal based game I created for this project.
I wanted to do something a little different for this project.
Most of the examples I saw were games such as battleship or hangman, or they
were very similar to the love sandwiches walkthrough which I wanted to stay away from.
This game is like an adventure game but with a competitive twist, the users scores
are sent to a Google sheet to display the current leaderboard.
As a golfer myself I wanted to make something that interested me and I could
share with my friends and see who could get the best score.

The deployed project can be viewed [here.](https://python-golf-7c3c839b8f7b.herokuapp.com/)

The leaderboard workbook can be viewed [here.](https://docs.google.com/spreadsheets/d/1_881-aBxzA8TwstEB7xGB9ZpJzDYFXvt9tCD4hYbZWU/edit#gid=0)

## Table of Contents

1. [User Experience](#user-experience)
    1. [Project Goals](#project-goals)
    2. [User Stories](#user-stories)
    3. [Data collection](#data-collection)
2. [Features](#features)
    1. [Title screen](title-screen)
    2. [Rules](#rules)
    3. [Holes](#holes)
    4. [Club Selection](#club-selection)
    5. [Shot Outcome](#shot-outcome)
    6. [Putting](#putting)
    7. [Game Summary](#game-summary)
    

## User Experience

### Project Goals

- Make a fun interactive golf game.

- Store data in a google sheet.

- Add some user options to make the game more interesting.

- Have a leaderboard to make it more competitive.

- Use different color text to differentiate between good and bad shots / results.

- Use ascii art to break up text and make it more fun.

### User Stories

- As a player, I want the game to have simple rules to follow.

- As a player, I want the game to be interesting and entertaining.

- As a player, I want the outcome of each shot to be clear to me.

- As a player, I want the controls to be easy.

- As a player, I want to be able to access a leaderboard.

- As a player, I want to be shown a summary of my round.

- As a player I want to be given the option to play again.

### Data Collection

![Leaderboard](assets/images/leaderboard.png)

- For this project I decided a Google sheet would be a good idea to add,
I learned a bit about this during the walkthrough and I wanted to test myself.

- In the workbook I have seperate leaderboards for 3-hole , 6-hole and 9-hole competitions.

- Once the user has finished the game the user name they entered along with their score is sent
to the correct sheet.

- I also used a script extension (see below) to order the leaderboards low - high as low score in golf wins.

![Script](assets/images/sheet_script.png)

## Features

### Title Screen

![title screen](assets/images/title.png)

- The title screen just shows the name of the game, I used ascii art from [Patorjk.com](https://patorjk.com/) to create this.

- The title screen remains for 5 seconds before the game begins.

- After the 5 seconds the user will be asked to enter their name for the leaderboard.(see below)

![name](assets/images/name.png)

### Rules

![rules](assets/images/rules.png)

- The rules section starts with welcoming the player to the game.

- It then follows on with the rules of the game, I tried to make these
eay to understand as I know not everyone is familiar with the rules of golf.

- It outlines the club choice the user will have to make and explains
what each choice does and how it could affect their score.

- Also explains the rule for the penalty applied when you enter a hazard.
As this is slighty different to how a real game of golf would go.

### Holes

![holes](assets/images/holes.png)

- The highlighted input asks the user to play 3,6 or 9 holes.

- Depending on the users selection the program will send their
data to the appropiate worksheet.

- There is a title above each hole showing the user what hole they are currently on.

### Club Selection

![tee shot](assets/images/tee_shot.png)

- The user is then prompted to select a club for the tee shot.

- The driver has a greater chance at a great shot but also a greater chance at entering a hazard.

- The iron is the safer shot, less chance at a great shot or hazards but a
greater chance at hitting the fairway.

- Entering the club you want only chooses the club, the user still has to press enter to hit the shot.

### Shot Outcome

![shot outcome](assets/images/shot_outcome.png)

- After each shot there is a swing message that comes up.

- The swing message is different depending on the type of shot.

- I have also included a ascii art drawing to simulate a golfer swinging a club.

- The outcome message is included below the ascii art, I have added color
to the message to help the user determine the outcome. It's as simple as green
is good and red is bad.

- Above the outcome was bad , I've added a good outcome below to demonstrate.

![good outcome](assets/images/good_outcome.png)

### Putting 

![putting start](assets/images/putt.png)

- The user has no choice of club on the greens, the only club permitted is the putter.

- So after the approach shot the user is prompted to press enter to hit their putt.

![putt message](assets/images/putt_outcome.png)

- There is a separate swing message for putting.

- I have added a different ascii art piece for the putter. It displays a putter a ball and the hole.

![short putt](assets/images/short_putt.png)

- If the initial putt is missed the user will be hitting a short putt.

- These type of putts have an increased probability of going in the hole.

- There is a small chance you miss these putts.

- In this case the user will be given a "gimme" as it's called in golf.
 This means you don't have to hit the shot as it's so close to the hole.
 But it will still count as a stroke. (see below)

 ![short miss](assets/images/short_miss.png)

 ### Game Summary

 ![game summary](assets/images/game_summary.png)

 - The game summary will display after you have played your last hole.

 - It contains the user name, score on each hole, total number of holes played and the total score.

 - It also asks the user to play again, which starts the program again from the start incase they would like to play more or less holes.

 ### Hazard

 ![hazard](assets/images/hazard.png)

 - If the user ends up in a hazard it's not realistic to apply real golf rules to this,
 so the user is just given a 1 stroke penalty. So if you hit the first shot into a hazard the 
 next shot you take will be your third.

 






