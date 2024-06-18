#for typehinting
class Team: pass
class Match: pass
class TimeSlot: pass
class Day: pass
class Comp: pass
"""
will read inputs from a file

Match:
    - team1
    - team2
    - winner
Timeslot:
    - Match
Day:
    - available courts
    - timeslots
Comp:
    - teams
    - days
Team:
    - single or doubles
    - player(s)
    - change __str__ method to print out team members
"""

class Match:
    def __init__(self, team1, team2):
        #TODO: add check that both teams are in the same comp
        self.team1 = team1
        self.team2 = team2
        self.winner = None

    def setWinner(self):
        print("Who won the match?")
        print(f"Teams:\n1. {self.team1}\n2. {self.team2}")
        winner = input("Enter 1 or 2 > ")
        #TODO: add "are you sure" check
        if winner in ["1", "2"]:
            self.winner = int(winner)

class Team:
    def __init__(self, players):
        self.players = players
        self.singles = len(players) == 1

    def __str__(self):
        msg = ""
        for player in self.players:
            msg += f"{player.name}, "
        return msg[:-2]

class Player:
    def __init__(self, name, gender):
        if len(name.split()) != 2:
            print(f"Please change the name {name} so that it is a first and last name.")
            exit()
        self.name = name
        gender = gender.upper()
        if gender not in ["M", "F"]:
            print(f"Gender: {gender} is not valid for player {name}")
            exit()
        self.gender = gender

class Day:
    def __init__(self, timeslots, courts: int):
        self.timeslots = timeslots
        self.courts = courts

class Timeslot:
    def __init__(self, match = None):
        self.match = match

    def isFree(self):
        return self.match

class Comp:
    def __init__(self, isSingles, teams, days):
        self.singles = isSingles
        self.teams = teams
        self.size = len(teams)
        self.days = days
