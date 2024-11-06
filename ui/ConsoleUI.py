from logic.SportsTeam import SportsTeam
from ui.input_validation import select_item, input_string
from logic.Conference import Conference
from data.Database import Database


class ConsoleUI:
    __all_conferences = []
    __all_teams = None

    @staticmethod
    def print_menu():
        print()
        print("Enter 'L' to list all Conferences.")
        print("Enter 'T' to display all teams.")
        print("Enter 'A' to add a basktetball team.")
        print("Enter 'J' to Join a team to a conference.")
        print("Enter 'X' to exit.")
        print("Enter 'Z' to delete a team.")
        print("Enter 'C' to add a basketball conference.")
        print("Enter 'D' to delete a conference.")
        print("Enter 'S' to show a conference.")
        print()



    @classmethod
    def init(cls):
        cls.__all_teams, cls.__all_conferences = Database.get_data()

    @classmethod
    def show_all_teams(cls):
        # We are going to loop through all teams and print out each one.
        for team in cls.__all_teams:
            print(team)

    @classmethod
    def list_all_conferences(cls):
        # We are going to loop through all conferences and print out each conference details.
        for conference in cls.__all_conferences:
            print(conference)

    @classmethod
    def add_team(cls):
        # Is what we want to create already in the team?
        # If Found then we want to print that the team already exists.
        # Team is the information provided to prove the team already exists.
        # If not found we want to store a new team in all_teams.
        team_name = input_string("Please enter the name of a professional basketball team: ", "Name cannot be non-empty.")
        location = input_string("Please enter the name of the teams location: ", "Name cannot be non-empty.")
        url = input_string("Please enter the URL for the top plays of the team you want to add: ")
        year_of_establishment = input_string("Please enter the year of establishment: ")
        note = input_string("Please include a note: ")

        found = False
        for team in cls.__all_teams:
            if team_name == team.get_name():
                found = True
                break

        if found == True:
            print("you have entered a team that already exists")
            return
        elif found == False:
            team = SportsTeam(team_name, location, url, year_of_establishment, note)
            cls.__all_teams.get_teams().append(team)
            print(f"{team.get_name()} has been added.")


    @classmethod
    def join_team(cls, team, conference):
       # cls.__all_teams.append(team)
        conference.add_team(team)
        print(f"{team.get_name()} has been added.")



    @classmethod
    def join_team_con(cls):
        conference_name = input_string("Please enter the name of the confernce the team will be added to.: ", "Name must be non-empty.")
        team_name = input_string("Please enter the name of the team being added.: ", "Name must be non-empty.")

        conference = ""

        for con in cls.__all_conferences:
            if con.get_name().lower() == conference_name.lower():
                conference = con

        team = ""

        for t in cls.__all_teams:
            if t.get_name().lower() == team_name.lower():
                team = t #

        if conference and team:
            cls.join_team(team, conference)

    @classmethod
    def create_conference(cls):
        name = input_string("Please enter the name of a professional basketball conference: ", "Name cannot be non-empty.")
        thumbnail = input_string("Please enter the URL for the top plays of the team you want to add: ")
        description = input_string("Enter the description for the conference: ", valid=lambda x: True)
        # teams = input_string("Please enter the name of the NBA Teams in the Eastern conference: ", "Name cannot be non-empty.")

        # Is what we want to create already in the conference?
        # What do we want to use from the information provided if the information already exists? __all_conferences
        # An information we can use to determine if the conference we want to create exists or not, is name.
        # Working with the name we asked the user to enter the conference name and we are going to search through all conferences
        # If found, then we will tell the user you have entered a confernece that exists already.
        # If not found then a new conference will be stored in all_conferences.
        found = False
        for conference in cls.__all_conferences:
            if name == conference.get_name():
                found = True
                break

        if found == True:
            print("you have entered a conference that exists already")
            return
        elif found == False:
            conference = Conferencl
            e(name, thumbnail, description, teams)
            cls.__all_conferences.append(conference)
            print("This new conference has been added to all conference list")

    @classmethod
    def delete_team(cls):
        team_name = input_string("Select the team you want to delete.")
        #Database.dselete_team(team_name)
        for x in cls.__all_teams:
            if x.get_name() == team_name:
                cls.__all_teams.remove(x)
                print()
                print("Team Has Been Delted")


    @classmethod
    def delete_playlist(cls):
        name = input_string("Please enter the name of the conference you want to delete: ", "Name must be non-empty.")

        for n in cls.__all_conferences:
            if n.get_name() == name.lower():
                cls.__all_conferences.remove(n)
                print("Conference has been deleted.")



        # Database.delete_playlist(name)

    @classmethod
    def show_playlist(cls):
        name = input_string("Please enter the name of the playlist you want to show: ", "Name must be non-empty.")

        for n in cls.__all_conferences:
            if n.get_name() == name.lower():
                print(n)

        # playlist = Database.get_playlist(name)
        #
        # if playlist is not None:
        #     print(playlist)
        # else:
        #     print("Playlist not found.")

    @classmethod
    def list_all_playlists(cls):
        conference = cls.__all_conferences
        if conference:
            for playlist in conference:
                print(playlist)
        else:
            print("No playlists available.")



    @classmethod
    def run(cls):
        while True:
            cls.print_menu()
            choice = select_item("Please select an item: ", "Error. Please type in a valid menu choice.",
                                 ['L', 'T', 'A', 'J', 'X', 'P', 'C', 'D', 'S', 'Z'])
            if choice == "L":
                cls.list_all_conferences()
            elif choice == "T":
                cls.show_all_teams()
            elif choice == "A":
                cls.add_team()
            elif choice == "J":
                cls.join_team_con()
            elif choice == "P":
                cls.list_all_playlists()
            elif choice == "Z":
                cls.delete_team()
            elif choice == "D":
                cls.delete_playlist()
            elif choice == "S":
                cls.show_playlist()
            elif choice == "C":
                cls.create_conference()
            elif choice == "X":
                break


if __name__ == "__main__":
    ConsoleUI.init()
    ConsoleUI.run()