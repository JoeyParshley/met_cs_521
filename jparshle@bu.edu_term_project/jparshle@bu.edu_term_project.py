"""
   Joey Parshley
   MET CS 521 O2
   28 APR 2018
   Final Project
   Description: Convert Team Scores to Offensive stats table

                :input : gamescore.csv a file containing the score sheets of 
                         several games for a team of players

"""
# import csv module and Player class
import csv
from player import Player

players = []

def getPlayers():
    """
    Definition: Reads the scores in for the players and creates a 
    list of players.
    """
    
    # open the csv file making sure the file can be opened
    try:
        f = open ('gamescore.csv')
    except IOError:
        print("Could not read {}".format('gamescore.csv'))
        sys.exit()

    with f:
        reader = csv.reader(f)
        # loop through each row the csv file
        for row in reader:
            # create a dictionary holding players name and their 
            # game performance
            player_dict = {'name':row[0], 'performance':row[1:]}
            # create a player object based off of the 
            player = Player(player_dict['name'], player_dict['performance'])
            # append the player object to the list of players
            players.append(player)


def displayResults():
    """
    Definition: Display the offensive stats for the players
    """
    print()
    print("{:<10} | {:^10} | {:^10} | {:^10} | {:^10} | {:^10}"\
        " | {:^10} | {:^10} | {:^10} | {:^10} | {:^10}"
        .format("Name","AB","H","2B","3B","HR","TB","AVG","OBP","SLG","OPS"))
    print("==================================================================="\
        "=====================================================================")

    # loop through the players list and display the stats for eac player
    for player in players:
        print("{:<10} | {:^10} | {:^10} | {:^10} | {:^10} | {:^10}"\
            " | {:^10} | {:^10.3f} | {:^10.3f} | {:^10.3f} | {:^10.3f}"
            .format(
                player.get_name(),
                player.get_at_bats(),
                len(player.get_total_hits()),
                player.get_doubles(),
                player.get_triples(),
                player.get_home_runs(),
                player.get_total_bases(),
                player.get_batting_average(),
                player.get_on_base_percentage(),
                player.get_slugging(),
                player.get_ops()
            ))
    print()
if __name__ == '__main__':
    getPlayers()

    displayResults()
