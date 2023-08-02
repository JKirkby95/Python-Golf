import gspread
from google.oauth2.service_account import Credentials
import random
import time
import colorama
colorama.init()
from colorama import Fore, Style


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
six_hole = SHEET.worksheet('6-Hole')
nine_hole = SHEET.worksheet('9-Hole')

def get_name():
    """
    This function gets the players name
    """
    name = input("What is your name? \n")

    return name

def tee_shot():
    """
    This function determines the outcome of your tee shot
    """
    outcome = random.choices(
        ["good_tee", "rough_tee", "great_tee", "hazard_tee"],
        [0.4, 0.4, 0.1, 0.1],   # Probabilities for each outcome
        k=1                      
    )[0]
    time.sleep(1)
    return outcome

def approach_shot():
    """
    This function determines the outcome of your approach shot
    """
    outcome = random.choices(
        ["good_approach", "rough_approach", "great_approach",
            "hazard_approach"],           
        [0.4, 0.4, 0.1, 0.1],   # Probabilities for each outcome
        k=1                      
    )[0]
    time.sleep(1)
    return outcome

def putter_shot():
    """
    this function determines the outcome of your short shot
    """
    outcome = random.choices(
        ["good_putt", "poor_putt", "in_the_hole"],
        [0.50, 0.20, 0.30],   # Probabilities for each outcome
        k=1                      
    )[0]
    time.sleep(1)
    return outcome

def short_putt():
    """
    this function determines the outcome of your short putt
    """
    outcome = random.choices(
        ["tap_in", "lip_out"],
        [0.95, 0.05],   # Probabilities for each outcome
        k=1                     
    )[0]
    time.sleep(1)
    return outcome

def swing_message():
    """
    This message adds some context to tee and approach shots
    """
    print("Swinging the club....\n")
    print("The ball is in the air....\n")

def putt_message():
    """
    This message adds some context to the putts
    """
    print("Lining up the putt....\n")
    print("It's rolling towards the hole....\n")

def play_again():
    while True:
        response = input("Would you like to play again? (yes/no): ").lower()
        if response == "yes":
            return True
        elif response == "no":
            return False
        else:
            print("Invalid response. Please enter 'yes' or 'no'.")

def main():
    """
    This function runs the game and displays the outcome of the shots
    """
    global total_score
    player_name = get_name()
    print(f"Hello {player_name}, welcome to Python Golf!\n")

    total_holes = int(
        input("How many holes do you want to play? (3, 6, or 9): "))
    while total_holes not in [3, 6, 9]:
        print("Invalid input. Please choose 3, 6, or 9 holes.")

    scores = {}  #List of scores for each hole
    total_score = 0  #Total score for the player

    for hole_number in range(1, total_holes + 1):
        print(f"\n--- Hole {hole_number} ---\n")

        score = 0
        input("Press Enter to hit the shot...\n")

        swing_message()
        shot_outcome = tee_shot()

        if shot_outcome == "good_tee":
            print(Fore.GREEN + "You hit a good tee shot! Safely down the middle of the fairway.\n" + Style.RESET_ALL)
            score += 1
        elif shot_outcome == "rough_tee":
            print(Fore.RED + "Your shot is in the rough.\n" + Style.RESET_ALL)
            score += 1
        elif shot_outcome == "great_tee":
            print(Fore.GREEN  + "Wow! A great shot!\n" + Style.RESET_ALL)
            score += 1
        else:
            print(Fore.RED + "Uh-oh! Your shot landed in a hazard!\n" + Style.RESET_ALL)
            score += 2

        input("Press Enter to hit the approach shot...\n")
        swing_message()
        approach_outcome = approach_shot()

        if approach_outcome == "good_approach":
            print(Fore.GREEN + "You made a good approach shot! The ball is on the green.\n" + Style.RESET_ALL)
            score += 1
        elif approach_outcome == "rough_approach":
            print(Fore.RED + "Your approach shot is in the rough.\n" + Style.RESET_ALL)
            score += 1
        elif approach_outcome == "great_approach":
            print(Fore.GREEN + "Amazing approach shot!\n" + Style.RESET_ALL)
            score += 1
        else:
            print(Fore.RED + "Oh no! Your approach shot ended up in a hazard!\n" + Style.RESET_ALL)
            score += 2

        input("Press Enter to hit your putt...\n")
        putt_message()
        putt_outcome = putter_shot()

        if putt_outcome == "good_putt":
            print(Fore.GREEN + "You made a good putt, you're 5 feet from the hole.\n" + Style.RESET_ALL)
            score += 1
        elif putt_outcome == "poor_putt":
            print(Fore.RED + "Poor putt.. you're still 10 feet from the hole.\n" + Style.RESET_ALL)
            score += 1
        elif putt_outcome == "in_the_hole":
            print(Fore.GREEN + "In the hole! Great putt.\n") + Style.RESET_ALL
            score += 1
            scores[f"Your score on hole {hole_number} "] = score
            print(f"Your score on Hole {hole_number}: {score}")
            continue  

        input("Press Enter to hit your short putt...\n")
        putt_message()
        tap_in_outcome = short_putt()

        if tap_in_outcome == "tap_in":
            print(Fore.GREEN + "Well done you got it in the hole!\n" + Style.RESET_ALL)
            score += 1
        else:
            print(Fore.RED + "Oh no... Your putt just missed\n" + Style.RESET_ALL)
            print(Fore.RED + "I'll give you that one no need to hit this shot" + Style.RESET_ALL)
            score += 2
            
        scores[f"Your score on hole {hole_number} "] = score

        print(f"Your score on Hole {hole_number}: {score}")

    total_score = sum(scores.values())

    print(f"\n--- Game Summary ---")
    print(f"Player Name: {player_name}")
    print("Hole Scores:")
    for hole, score in scores.items():
        print(f"{hole}: {score}")
    print(f"Total Score: {total_score}")

    row_data = [player_name, total_score]
    three_hole.append_row(row_data)

if __name__ == "__main__":
    while True:
        main()

        if not play_again():
            break
