import json

from view.review_v import ReviewView


class ReviewController:
    """Data access"""

    def __init__(self):
        pass

    def general_responses(self):
        """user-selected routing from the review_v"""

        user_input = ReviewView().general_information()

        try:
            if user_input == "1":
                """Call fonction to see a player's result"""
                ReviewT1().print_tournament_1()
                self.general_responses()

            elif user_input == "2":
                """Call fonction to see round 1 results"""
                ReviewT2().print_tournament_2()
                self.general_responses()

            elif user_input == "3":
                """Pass to end the tournament"""
                ReviewT3().print_tournament_3()
                self.general_responses()

            elif user_input == "Out":
                return

            elif user_input != "1" or "2" or "3" or "Out":
                print("ERREUR : Votre réponse n'est pas valable.")
                self.general_responses()

        except TypeError or ValueError:
            print(f"Votre réponse n'est pas valable, tapez 1, 2, 3, 4, 5 ou 6 {self.general_responses()}")

    @staticmethod
    def load_tournament_data():
        """Load tournament data"""

        with open("data/tournament_data.json") as f:
            tournaments = json.loads(f.read())

            return tournaments


class ReviewT1:

    def __init__(self):
        pass

    @staticmethod
    def clean_tournament_1():
        """Clean the tournament 1 name"""

        tournaments = ReviewController.load_tournament_data()[0]

        name = tournaments["Nom"]
        lower_name = name.lower()
        cleaner_name = (lower_name
                        .replace(" ", "_")
                        .replace("'", "_")
                        .replace("-", "_")
                        .replace(".", "")
                        .replace("é", "e")
                        .replace("è", "e")
                        .replace("ê", "e")
                        .replace("ô", "o")
                        .replace("à", "a")
                        .replace("â", "a"))

        return cleaner_name

    def load_tournament_1(self):
        """Load data from tournament 1"""

        with open(f"data/{self.clean_tournament_1()}/player_data_{self.clean_tournament_1()}.json") as f:
            players = json.loads(f.read())

            return players

    def print_tournament_1(self):
        """Print the tournament 1 result sorted by point"""

        players = self.load_tournament_1()

        print(f"\n====={self.clean_tournament_1()}=====")
        for number in range(len(players)):
            print("\n---{} {}---\n"
                  "-est né le {}\n"
                  "-son ID est {}\n"
                  "-possède {} points elo\n"
                  "-possède actuellement {} points de tournoi".format(
                   players[number].get("Prenom"),
                   players[number].get("Nom"),
                   players[number].get("Date de naissance"),
                   players[number].get("ID"),
                   players[number].get("Elo"),
                   players[number].get("Point")))


class ReviewT2:

    def __init__(self):
        pass

    @staticmethod
    def clean_tournament_2():
        """Clean the tournament 2 name"""

        tournaments = ReviewController.load_tournament_data()[1]

        name = tournaments["Nom"]
        lower_name = name.lower()
        cleaner_name = (lower_name
                        .replace(" ", "_")
                        .replace("'", "_")
                        .replace("-", "_")
                        .replace(".", "")
                        .replace("é", "e")
                        .replace("è", "e")
                        .replace("ê", "e")
                        .replace("ô", "o")
                        .replace("à", "a")
                        .replace("â", "a"))

        return cleaner_name

    def load_tournament_2(self):
        """Load data from tournament 2"""

        with open(f"data/{self.clean_tournament_2()}/player_data_{self.clean_tournament_2()}.json") as f:
            players = json.loads(f.read())

            return players

    def print_tournament_2(self):
        """Print the tournament 1 result sorted by point"""

        players = self.load_tournament_2()

        print(f"\n====={self.clean_tournament_2()}=====")
        for number in range(len(players)):
            print("\n---{}er/ème - {} {}---\n"
                  "-est né le {}\n"
                  "-son ID est {}\n"
                  "-possède {} points elo\n"
                  "-possède actuellement {} points de tournoi".format(
                   number + 1,
                   players[number].get("Prenom"),
                   players[number].get("Nom"),
                   players[number].get("Date de naissance"),
                   players[number].get("ID"),
                   players[number].get("Elo"),
                   players[number].get("Point")))


class ReviewT3:

    def __init__(self):
        pass

    @staticmethod
    def clean_tournament_3():
        """Clean the tournament 3 name"""

        tournaments = ReviewController.load_tournament_data()[2]

        name = tournaments["Nom"]
        lower_name = name.lower()
        cleaner_name = (lower_name
                        .replace(" ", "_")
                        .replace("'", "_")
                        .replace("-", "_")
                        .replace(".", "")
                        .replace("é", "e")
                        .replace("è", "e")
                        .replace("ê", "e")
                        .replace("ô", "o")
                        .replace("à", "a")
                        .replace("â", "a"))

        return cleaner_name

    def load_tournament_3(self):
        """Load data from tournament 3"""

        with open(f"data/{self.clean_tournament_3()}/player_data_{self.clean_tournament_3()}.json") as f:
            players = json.loads(f.read())

            return players

    def print_tournament_3(self):
        """Print the tournament 1 result sorted by point"""

        players = self.load_tournament_3()

        print(f"\n====={self.clean_tournament_3()}=====")
        for number in range(len(players)):
            print("\n---{}er/ème - {} {}---\n"
                  "-est né le {}\n"
                  "-son ID est {}\n"
                  "-possède {} points elo\n"
                  "-possède actuellement {} points de tournoi".format(
                   number + 1,
                   players[number].get("Prenom"),
                   players[number].get("Nom"),
                   players[number].get("Date de naissance"),
                   players[number].get("ID"),
                   players[number].get("Elo"),
                   players[number].get("Point")))
