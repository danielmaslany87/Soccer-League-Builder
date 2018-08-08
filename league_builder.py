# Soccer League Builder...
#                 ...a Teamtreehouse Project
#                                 by Daniel Maslany
#

# First we import the modules we need to operate on CSV files,
# and another one to return a date.
import csv
import datetime

# Here I declared a function that takes the file name as the parameter.
# The CSV readers goes through each line and creates a list of it, at the
# end, wrapping everything in a list.
# Next I've declared a dictionary that has two keys "Experienced" and
# "Beginner", each of them having an empty list valueself.
# The for loop goes through every position(index) which is a player in the list of
# unsorted_players list.
# it sorts the players depending if the condition is True(players experience is
# equal to YES) or false(the oposit to YES)
# returns "sorted" a dictionary with all  the players sorted in regards to their experienced

def import_players(name_file):
    with open(name_file) as csvfile:
        player_reader = csv.reader(csvfile, delimiter=',')
        unsorted_players = list(player_reader)
        sorted = {
        'Experienced': [],
        'Beginner': []
        }
        for player in unsorted_players:
            if player[2] == 'YES':
                sorted['Experienced'].append(player)
            else:
                sorted['Beginner'].append(player)
        return sorted

# This function takes two dict parameters, the sorted dict with out players and
# a dictionary containing three team names asigned as keys with values set to empty lists
# the while loop goes into each of the sorted lists and uses the pop() method to remove
# the last player from that list and append it to one of the team keys as its value
# I used the pop() method so I wont get anny duplicates.
# When both of the lists are empty (checked it by getting the len of each list and making sure its equal to zero)
# if this condition happens the while loop returns the teams dictionary and breaks

def assign_team(sorted_players, teams):
    experienced = list(sorted_players['Experienced'])
    beginner = list(sorted_players['Beginner'])
    while True:
        for team, players in teams.items():
            teams[team].append(experienced.pop())
            teams[team].append(beginner.pop())
        if (len(experienced) and len(beginner)) == 0:
            return teams
            break

# Function bellow takes the dictionary with all the sorted players that are assigned to their teams and
# creates a new file called |teams.txt| where first it writes the name of the team and under the name all the
# players, their experience and guardian name.

def write_teams_file(assigned_teams):
    file = open("teams.txt", "w")
    for team, list in teams.items():
        file.write(team + "\n")
        for player in list:
            file.write("{name}, {exp}, {guardian}\n".format(name=player[0], exp=player[2], guardian=player[3]))
    file.close()

# This function creates a welcome letter for each player. The file name has the whitespace replaced with a underscore
# Finally in this function I use the datetime module that I imported at the beggining.

def welcome_letter(assigned_teams):
    meeting = datetime.date.today() + datetime.timedelta(days=5)
    for team, list in teams.items():
        for player in list:
            player_file = open(player[0].replace(" ", "_") + ".txt", "w")
            player_file.write("Dear {},\n".format(player[3]) +
                                "Your child {} was successful in joining".format(player[0]) +
                                " the '{}' soccer team! ".format(team) + "\n" +
                                "The first team meeting will be on the {}, 9:00 AM.".format(meeting) +
                                "\nGood luck!")

if __name__ == "__main__":
# Assigning each key name to a team name as mentioned above.
    teams = {
    'Sharks': [],
    'Dragons': [],
    'Raptors': []
    }
    sorted = import_players("soccer_players.csv")
    assigned_teams = assign_team(sorted, teams)
    write_teams_file(assigned_teams)
    welcome_letter(assigned_teams)
