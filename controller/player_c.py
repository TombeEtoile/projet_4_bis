import json
from circular_import import TrafficCircle

from view.player_v import PlayerView, PlayerInstantiate


class PlayerController:

    def __init__(self):
        pass

    def player_answer(self):

        response = PlayerView.player_questions()

        try:
            if response == "1":
                """add player"""
                self.add_player()

            elif response == "2":
                """check list of player"""
                self.list_all_players()

            elif response == "3":
                """modify player list"""
                self.edit_player()

            elif response == "4":
                """delete player in the list"""
                self.delete_player()

            elif response == "5":
                """Return to menu"""
                self.return_to_menu()

            elif response != "1" or "2" or "3" or "4" or "5":
                print("ERREUR : Vous devez écrire 1, 2, 3, 4 ou 5")
                self.player_answer()

        except ValueError:
            print("ERREUR : Vous devez écrire 1, 2, 3, 4 ou 5")
            self.player_answer()

    @staticmethod
    def load_data():

        with open("../player_data.json") as f:
            players = json.loads(f.read())

            return players

    def add_player(self):

        new_player = PlayerInstantiate.get_player_data()

        with open("../player_data.json", "ab+") as f:
            if f.tell() == 2:
                f.seek(-2, 2)
                f.truncate()
                f.write(b'[\n')
            else:
                f.seek(-2, 2)
                f.truncate()
                f.write(b',\n')
            f.write(json.dumps(new_player, indent=2).encode())
            f.write(b'\n]')

        self.player_answer()

    def list_all_players(self):
        players = self.load_data()
        for player in range(len(players)):
            print("\n---Joueur n°{} - {} {}---\n"
                  "-est né le {}\n"
                  "-son ID est {}\n"
                  "-possède {} points elo\n"
                  "-possède actuellement {} points de tournoi".format(
                   player + 1,
                   players[player].get("Prenom"),
                   players[player].get("Nom"),
                   players[player].get("Date de naissance"),
                   players[player].get("ID"),
                   players[player].get("Elo"),
                   players[player].get("Point")))

    def edit_player(self):
        pass

    def delete_player(self):
        pass

    @staticmethod
    def return_to_menu():

        menu = TrafficCircle()
        menu.player_to_menu()


test = PlayerController()
test.player_answer()
# test.add_player()
# test.list_all_players()
