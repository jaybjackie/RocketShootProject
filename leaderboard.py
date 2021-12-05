import turtle
import json

from aircraft import Aircraft
from turtle import Turtle

class Leaderboard:
    """ Initailize Leaderboard window and update ranking."""
    def __init__(self, player, player_name) -> None:
        if not isinstance(player, Aircraft):
            raise TypeError("Invaild type object.")
        self.name = player_name
        self.score = player.score

    def insert(self):
        """Insert player name and player score into the database """
        new_data = {
            self.name:{
                "score": self.score
            }
        }

        try:
            with open('leaderboard.json','r') as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            with open('leaderboard.json','w') as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            data.update(new_data)
            with open('leaderboard','w') as data_file:
                json.dump(data, data_file, indent=4)


    # get top 3 player soon...

