import gspread
from google.oauth2.service_account import Credentials
import random
import time
import colorama
from colorama import Fore, Style
colorama.init()

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
    This function gets the players name for the leaderboard
    """
    while True:
        name = input("Please enter a user name for our leaderboard.\n")
        if name:
            return name
        else:
            print("Please enter a name, can't be blank.\n")


def tee_shot():
    """
    This function determines the outcome of your tee shot
    """
    choice = ""
    while choice not in ["driver", "iron"]:
        choice = input(
            "Select which club you'd like to use." +
            "(driver/iron): \n"
            )
        if choice not in ["driver", "iron"]:
            print("Invalid input please select driver or iron.\n")

    if choice == "driver":
        outcome = random.choices(
            ["good_tee", "rough_tee", "great_tee", "hazard_tee"],
            [0.3, 0.4, 0.2, 0.1],  # Adjusted probabilities for a driver shot
            k=1
        )[0]
    elif choice == "iron":
        outcome = random.choices(
            ["good_tee", "rough_tee", "great_tee", "hazard_tee"],
            [0.4, 0.4, 0.1, 0.1],  # Adjusted probabilities for an iron shot.
            k=1
        )[0]
    time.sleep(1)
    return outcome


def approach_shot():
    """
    This function determines the outcome of your approach shot
    """
    choice = ""
    while choice not in ["wood", "iron"]:
        choice = input(
            "Select which club you'd like to use. (wood/iron): \n"
            )
        if choice not in ["wood", "iron"]:
            print("Invalid input please select wood or iron.\n")

    if choice == "wood":
        outcome = random.choices(
            ["good_approach", "rough_approach",
             "great_approach", "hazard_approach"],
            [0.1, 0.2, 0.35, 0.35],   # Probabilities for each outcome
            k=1
        )[0]
    elif choice == "iron":
        outcome = random.choices(
            ["good_approach", "rough_approach",
             "great_approach", "hazard_approach"],
            [0.5, 0.2, 0.2, 0.1],   # Probabilities for each outcome
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

    ascii_art1 = Fore.GREEN + r"""
       \                   .  .                        |>>>
        \              .         ' .                   |
        O>>         .                 'o               |
        \       .                                      |
        /\    .                                        |
       / /  .'                                         |
    ^^^^^^^`^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    """ + Style.RESET_ALL
    print(ascii_art1)


def putt_message():
    """
    This message adds some context to the putts
    """
    print("Lining up the putt....\n")
    print("It's rolling towards the hole....\n")
    ascii_art2 = Fore.GREEN + r'''
                        |H|
                        |H|
                        |||
                        |||
                        |V|
                        | |
          .----=--.-':'-; <
         /=====  /'.'.'.'\ |
        |====== |.'.'.'.'.||             ___________
         \=====  \'.'.'.'/ /          .o8888888888888o.
          '--=-=-='-:.:-'-`           88888888888888888
                                      `Y8888888888888P`
                                        `"""""""""""`
        ''' + Style.RESET_ALL
    print(ascii_art2)


def play_again():
    while True:
        response = input(
            "Would you like to play again? (yes/no): "
            ).lower()
        if response == "yes":
            return True
        elif response == "no":
            return False
        else:
            print(
                "Invalid response. Please enter 'yes' or 'no'."
                )


def title():
    ascii_title = Fore.GREEN + r'''
    '    ____          _    _                      ____         _   __
    '   |  _ \  _   _ | |_ | |__    ___   _ __    / ___|  ___  | | / _|
    '   | |_) || | | || __|| '_ \  / _ \ | '_ \  | |  _  / _ \ | || |_
    '   |  __/ | |_| || |_ | | | || (_) || | | | | |_| || (_) || ||  _|
    '   |_|     \__, | \__||_| |_| \___/ |_| |_|  \____| \___/ |_||_|
    '           |___/
    ''' + Style.RESET_ALL
    print(ascii_title)
    time.sleep(5)


def main():
    """
    This function runs the game and displays the outcome of the shots
    """
    title()
    global total_score
    player_name = get_name()
    print(f"Hello {player_name}, welcome to Python Golf!\n")
    print(
        Fore.YELLOW +
        "Python Golf is a simple game the rules are as follows... \n"
        )
    print(
        "For tee shots you can choose to play a driver \n" +
        "or a safer iron shot. Driver shots could be rewarded with \n" +
        "a great shot but also have a higher probability " +
        "of entering a hazard.\n"
     )
    print("")
    print(
        "For approach shots you can choose between \n" +
        "a wood or an iron. The wood is like a driver it gives \n" +
        "a higher probability of a great shot but also gives \n" +
        "a higher probability of entering a hazard \n"
    )
    print("")
    print(
        "If you enter a hazard you will receive a one shot penalty.\n"
        )
    print("")
    print(
        "On the green you are only permitted to use a putter \n" +
        "so there is no choice of clubs there.\n"
    )
    print("")
    print(
        "At the end of each hole you will be informed of the score you got. \n"
        )
    print("")
    print(
        "And at the end of the game you will be told your final \n" +
        "score and find a link to the leaderboard google sheet. \n"
        + Style.RESET_ALL
        )

    total_holes = ""

    while total_holes not in ["3", "6", "9"]:
            total_holes = input(
            "How many holes do you want to play? (3, 6, or 9): \n"
        )
        if total_holes not in ["3", "6", "9"]:
            print("Invalid input. Please choose 3, 6, or 9 holes. \n")

    scores = {}  # List of scores for each hole
    total_score = 0  # Total score for the player

    for hole_number in range(1, int(total_holes) + 1):
        print(f"\n--- Hole {hole_number} ---\n")

        shot_outcome = tee_shot()

        score = 0
        input("Press Enter to hit the shot...\n")
        time.sleep(3)
        swing_message()

        if shot_outcome == "good_tee":
            print(
                Fore.GREEN +
                "You hit a good tee shot!" +
                "Safely down the middle of the fairway.\n"
                + Style.RESET_ALL
                )
            score += 1
        elif shot_outcome == "rough_tee":
            print(
                Fore.RED +
                "Your shot is in the rough.\n"
                + Style.RESET_ALL
                )
            score += 1
        elif shot_outcome == "great_tee":
            print(
                Fore.GREEN +
                "Wow! A great shot!\n"
                + Style.RESET_ALL
                )
            score += 1
        else:
            print(
                Fore.RED +
                "Uh-oh! Your shot landed in a hazard!\n"
                + Style.RESET_ALL
                )
            score += 2

        approach_outcome = approach_shot()

        input("Press Enter to hit the approach shot...\n")
        time.sleep(3)
        swing_message()

        if approach_outcome == "good_approach":
            print(
                Fore.GREEN +
                "You made a good approach shot! The ball is on the green.\n"
                + Style.RESET_ALL
            )
            score += 1
        elif approach_outcome == "rough_approach":
            print(
                Fore.RED +
                "Your approach shot is in the rough.\n"
                + Style.RESET_ALL
            )
            score += 1
        elif approach_outcome == "great_approach":
            print(
                Fore.GREEN +
                "Amazing approach shot!\n"
                + Style.RESET_ALL
            )
            score += 1
        else:
            print(
                Fore.RED +
                "Oh no! Your approach shot ended up in a hazard!\n"
                + Style.RESET_ALL
            )

            score += 2

        input("Press Enter to hit your putt...\n")
        putt_message()
        putt_outcome = putter_shot()

        if putt_outcome == "good_putt":
            print(
                Fore.GREEN +
                "You made a good putt, you're 5 feet from the hole.\n"
                + Style.RESET_ALL
            )
            score += 1
        elif putt_outcome == "poor_putt":
            print(
                Fore.RED +
                "Poor putt.. you're still 10 feet from the hole.\n"
                + Style.RESET_ALL
            )
            score += 1
        elif putt_outcome == "in_the_hole":
            print(
                Fore.GREEN +
                "In the hole! Great putt.\n"
                + Style.RESET_ALL
            )
            score += 1
            scores[f"Your score on hole {hole_number} "] = score
            print(f"Your score on Hole {hole_number}: {score}")
            continue

        input("Press Enter to hit your short putt...\n")
        putt_message()
        tap_in_outcome = short_putt()

        if tap_in_outcome == "tap_in":
            print(
                Fore.GREEN +
                "Well done you got it in the hole!\n"
                + Style.RESET_ALL
            )
            score += 1
        else:
            print(
                Fore.RED +
                "Oh no... Your putt just missed\n"
                + Style.RESET_ALL
            )
            print(
                Fore.RED +
                "I'll give you that one no need to hit this shot"
                + Style.RESET_ALL
            )
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
    if total_holes == "3":
        three_hole.append_row(row_data)
    elif total_holes == "6":
        six_hole.append_row(row_data)
    elif total_holes == "9":
        nine_hole.append_row(row_data)


if __name__ == "__main__":
    while True:
        main()

        if not play_again():
            break
