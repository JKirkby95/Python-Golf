import gspread
from google.oauth2.service_account import Credentials
import random

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
    This function starts the game
    """
    name = input("What is your name? ")

    return name

    
def tee_shot():
    outcome = random.choices(
        [1, 2, 3, 4],           # Possible outcomes: 1, 2, 3, 4
        [0.4, 0.4, 0.1, 0.1],   # Probabilities for each outcome
        k=1                      # Number of selections to make (1 shot)
    )[0]
    return outcome

def main():
    score = 0
    player_name = get_name()

    print(f"Hello {player_name}, welcome to Python Golf!")
    input("Press Enter to hit the shot...")

    shot_outcome = tee_shot()

    if shot_outcome == 1:
        print("You hit a good shot!")
        score =+ 1
    elif shot_outcome == 2:
        print("Your shot is in the rough.")
        score =+ 1
    elif shot_outcome == 3:
        print("Wow! A great shot!")
        score =+ 1
    else:
        print("Uh-oh! Your shot landed in a hazard!")
        score =+ 2


    print(score)

if __name__ == "__main__":
    main()
    

