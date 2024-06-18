import os
import re
from classes import *
# Information outside of teams/courts headers will be ignored

def parse(filepath):
    """
    filepath should be in format [M|F|X][singles|doubles].txt
    where X is mixed
    """
    try:
        file = open(filepath, "r")
    except FileNotFoundError:
        print(f"Could not find file {filepath}")
        exit()

    badFilepath = False
    if filepath[0].upper() not in ["M", "F", "X"]:
        badFilepath = True

    if filepath[1:-4].lower() not in ["singles", "doubles"]:
        badFilepath = True

    if filepath[-4:] != ".txt":
        badFilepath = True

    if badFilepath:
        msg = f"Sorry, your entered file {filepath} is not valid, please "
        msg += "refer to documentation to find proper format"
        print(msg)
        exit()


    gender = filepath[0].upper()
    size = filepath[1:-4].lower()

    courts = 0
    teams = []
    teamsHeader = False
    daysHeader = False
    days = []
    lineNo = 0
    while (line := file.readline()):
        line = line.rstrip()
        lineNo += 1
        if line == "": 
            continue
        if line == "Teams:":
            teamsHeader = True
            daysHeader = False
            continue
        if line.startswith("Day ") and line.endswith(":"):
            daysHeader = True
            teamsHeader = False
            continue

        if teamsHeader:
            players = [name.strip() for name in line.split(",")]
            players = checkValidPlayers(players)
            checkValidTeams(players, size)
            teams.append(Team(players))

        elif daysHeader:
            for i in range(2):
                line = file.readline().rstrip()
                lineNo += 1
                if not line:
                    printExit(f"Incomplete day section at line No. {lineNo}")
                if not (num := getEndNum(line)):
                    printExit("No number at line No. {lineNo}")
                if line.startswith("timeslots:"):
                    timeslots = num
                elif line.startswith("courts:"):
                    courts = num
                else:
                    msg = f"Line No. {lineNo} is invalid, please refer to documentation"
                    printExit(msg)

    return Comp(
            isSingles = (size == "singles"),
            teams = teams,
            days = days
            )

def getEndNum(line):
    return re.sub(r"[^\d]", "", line)

def checkValidTeams(players, size):
    if size == "singles" and len(players) != 1:
        msg = f"You entered the team {players} with size "
        msg += f"{len(players)} into a singles comp, please enter"
        msg += "a team with one player"
        print(msg)
        exit()
    elif size == "doubles" and len(players) != 2:
        msg = f"You entered the team {players} with size "
        msg += f"{len(players)} into a doubles comp, please enter"
        msg += "a team with two players"
        print(msg)
        exit()

def checkValidPlayers(players):
    newPlayers = []
    for player in players:
        if len(player.split()) != 2:
            print(f"Player '{player}' needs a first and last name")
            exit()
        newPlayers.append(" ".join(player.split()))
    return newPlayers

def printExit(msg):
    print(msg)
    exit()
