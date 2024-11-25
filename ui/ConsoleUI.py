from logic.SportsTeam import SportsTeam
from ui.input_validation import select_item, input_string
from logic.PerformanceST import PerformanceST
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
        cls.__all_teams, cls.__all_conferences = Database.read_data() #was origianlly get_data.. lab 6 changes

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
        # key = PerformanceST.make_key(team_name, location, url, current_record)  #Might need to switch to PerformanceST
        # teamkey = SportsTeam.lookup(key)
        # if teamkey is not None:
        #     print("\nERROR! Record entry already exists!")
        #     return

        url = input_string("Please enter the URL for the top plays of the team you want to add: ")
        year_of_establishment = input_string("Please enter the year of establishment: ")
        current_record = input_string("Please include a note: ")
        key = PerformanceST.make_key(team_name, location, url, current_record)  # Might need to switch to PerformanceST
        teamkey = SportsTeam.lookup(key)
        if teamkey is not None:
            print("\nERROR! Record entry already exists!")
            return


#        found = False
#        for team in cls.__all_teams:
#            if team_name == SportsTeam.get_name():
#                found = True
#                break

        # if found == True:
        #     print("you have entered a team that already exists")
        #     return
        # elif found == False:
        team = PerformanceST(team_name, location, url, year_of_establishment, current_record)
        cls.__all_teams.get_teams().append(team)
        team.save()
        print(f"{team.get_name()} has been added.")

    @classmethod
    def join_team(cls, team, conference):
        # cls.__all_teams.append(team)
        conference.append(team)
        print(f"{team.get_name()} has been added.")

    @classmethod
    def join_team_con(cls):
        conference_name = input_string("Please enter the name of the conference the team will be added to: ",
                                       "Name must be non-empty.")
        team_name = input_string("Please enter the name of the team being added: ",
                                 "Name must be non-empty.")

        conference = ""  # Initialize with "" to check later
        for con in cls.__all_conferences:
            if con.get_name().lower() == conference_name.lower():
                conference = con
                break  # Exit the loop once the conference is found

        team = ""  # Initialize with "" to check later
        for t in cls.__all_teams:  # Use 't' instead of 'team' to avoid confusion
            if t.get_name().lower() == team_name.lower():
                team = t
                break  # Exit the loop once the team is found

        if conference and team:  # Check if both conference and team were found
            cls.join_team(team, conference)  # Call the join_team method
        else:
            print("Either the conference or the team does not exist.")

    # @classmethod
    # def create_conference(cls):
    #     # name, videos, thumbnail, description
    #     name = input_string("Please enter the name of the conference or 'None' to exit: ", "Name must be non-empty.")
    #     if name == "None":
    #         return
    #     conference = Conference.lookup(name)
    #     if conference is not None:
    #         print("Error! Playlist already exists.")
    #         return
    #     thumbnail = input_string("Please enter 'top 5 dunks'. : ", "Name must be non-empty.")
    #     description = input_string("Where are the teams being stored? : ")
    #     teams = input_string("Please enter the team name in the conference. : ", valid=lambda x: True)
    #     conference = Conference(name, thumbnail, description, teams, save=True)
    #     cls.__all_playlists.append(conference)
    #     print("Playlist created.")

    # @classmethod
    # def create_conference(cls):
    #     name = input_string("Please enter the name of a professional basketball conference: ", "Name cannot be non-empty.")
    #     thumbnail = input_string("Please enter the URL for the top plays of the team you want to add: ")
    #     description = input_string("Enter the description for the conference: ", valid=lambda x: True)
    #     teams = input_string("Please enter the name of the NBA Teams in the Eastern conference: ", "Name cannot be non-empty.")

        # Is what we want to create already in the conference?
        # What do we want to use from the information provided if the information already exists? __all_conferences
        # An information we can use to determine if the conference we want to create exists or not, is name.
        # Working with the name we asked the user to enter the conference name and we are going to search through all conferences
        # If found, then we will tell the user you have entered a confernece that exists already.
        # If not found then a new conference will be stored in all_conferences.
        # found = False
        # for conference in cls.__all_conferences:
        #     if name == conference.get_name():
        #         found = True
        #         break
        #
        # if found == True:
        #     print("you have entered a conference that exists already")
        #     return
        # elif found == False:
        #     conference = Conference(name, thumbnail, description, teams)
        #     conference.save()       # new addition to lab 6
        #     cls.__all_conferences.append(conference)
        #     print("This new conference has been added to all conference list")

    @classmethod
    def create_conference(cls):
        name = input_string("Please enter the name of the new conference we are adding. : ",
                                 "Name cannot be non-empty.")
        thumbnail = input_string("Please enter the phrase 'top 5 dunks'. : ", "Name cannot be non-empty.")
        # key = PerformanceST.make_key(team_name, location, url, current_record)  #Might need to switch to PerformanceST
        # teamkey = SportsTeam.lookup(key)
        # if teamkey is not None:
        #     print("\nERROR! Record entry already exists!")
        #     return

        description = input_string("what conference the teams will be stored in 'teams in the ___' be stored in: ")
        team_name = input_string("enter the name of teams in conference: ")
        team = ConsoleUI.get_team_by_name(team_name)
        teams = []
        if team is not None:
            teams.append(team)
            team.save()
        # key = Conference.get_id(teams)  # Might need to switch to PerformanceST
        # teamkey = Conference.lookup(key)
        # if teamkey is not None:
        #     print("\nERROR! Record entry already exists!")
        #     return

        #        found = False
        #        for team in cls.__all_teams:
        #            if team_name == SportsTeam.get_name():
        #                found = True
        #                break

        # if found == True:
        #     print("you have entered a team that already exists")
        #     return
        # elif found == False:
        conference = Conference(name, thumbnail, description, teams)
        key = conference.get_id()  # Might need to switch to PerformanceST
        teamkey = conference.lookup(key)
        if teamkey is not None:
            print("\nERROR! Record entry already exists!")
            return
        cls.__all_conferences.append(conference)
        print(f"{conference.get_name()} has been added.")

    @classmethod
    def get_team_by_name(cls, team_name):
        for team in cls.__all_teams:
            if team.get_name() == team_name:
                return team
        return None

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