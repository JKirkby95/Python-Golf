import gspread
from google.oauth2.service_account import Credentials
import random
import time

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('Python-Golf-Leaderboard')

three_hole = SHEET.worksheet('3-Hole')

def get_name():
    """
    This function gets the players name
    """
    name = input("What is your name? ")

    return name

    
def tee_shot():
    """
    This function determines the outcome of your tee shot
    """
    outcome = random.choices(
        ["good_tee", "rough_tee", "great_tee", "hazard_tee"],           # Possible outcomes: 1, 2, 3, 4
        [0.4, 0.4, 0.1, 0.1],   # Probabilities for each outcome
        k=1                      # Number of selections to make (1 shot)
    )[0]
    time.sleep(2)
    return outcome

def approach_shot():
    """
    This function determines the outcome of your approach shot
    """
    outcome = random.choices(
        ["good_approach", "rough_approach", "great_approach", "hazard_approach"],           # Possible outcomes: 1, 2, 3, 4
        [0.4, 0.4, 0.1, 0.1],   # Probabilities for each outcome
        k=1                      # Number of selections to make (1 shot)
    )[0]
    time.sleep(2)
    return outcome

def putter_shot():
    """
    this function determines the outcome of your short shot
    """
    outcome = random.choices(
        ["good_putt", "poor_putt", "in_the_hole"],           # Possible outcomes: 1, 2, 3, 4
        [0.50, 0.20, 0.30],   # Probabilities for each outcome
        k=1                      # Number of selections to make (1 shot)
    )[0]
    time.sleep(2)
    return outcome

def swing_message():
    """
    This message adds some context to tee and approach shots
    """
    print("Swinging the club....")
    print("")
    print("The ball is in the air....")

def putt_message():
    """
    This message adds some context to the putts
    """
    print("Lining up the putt....")
    print("")
    print("It's rolling towards the hole....")

def main():
    """
    This function runs the game and displays the outcome of the shots
    """
    score = 0
    player_name = get_name()

    print(f"Hello {player_name}, welcome to Python Golf!")
    input("Press Enter to hit the shot...")

    swing_message()
    shot_outcome = tee_shot()

    if shot_outcome == "good_tee":
        print("You hit a good tee shot! Safely down the middle of the fairway.")
        score =+ 1
    elif shot_outcome == "rough_tee":
        print("Your shot is in the rough.")
        score =+ 1
    elif shot_outcome == "great_tee":
        print("Wow! A great shot!")
        score =+ 1
    else:
        print("Uh-oh! Your shot landed in a hazard!")
        score =+ 2

    input("Press Enter to hit the approach shot...")
    swing_message()
    approach_outcome = approach_shot()

    if approach_outcome == "good_approach":
        print("You made a good approach shot! The ball is on the green.")
        score += 1
    elif approach_outcome == "rough_approach":
        print("Your approach shot is in the rough.")
        score += 1
    elif approach_outcome == "great_approach":
        print("Amazing approach shot!")
        score += 1
    else:
        print("Oh no! Your approach shot ended up in a hazard!")
        score += 2

    input("Press Enter to hit your putt...")
    putt_message()
    putt_outcome = putter_shot()

    if putt_outcome == "good_putt":
        print("You made a good putt, you're 5 feet from the hole.")
        score += 1
    elif putt_outcome == "poor_putt":
        print("Poor putt.. you're still 10 feet from the hole.")
        score += 1
    elif putt_outcome == "in_the_hole":
        print("In the hole! Great putt.")
        score += 1

    print(f"Your score: {score}")

if __name__ == "__main__":
    main()
    

