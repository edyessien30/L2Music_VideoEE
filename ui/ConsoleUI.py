from logic.SportsTeam import SportsTeam
from ui.input_validation import select_item, input_string
from logic.PlayList import PlayList
from data.Database import Database


class ConsoleUI:
    @staticmethod
    def print_menu():
        print("Enter 'L' to list the west coast NBA teams performance.")
        print("Enter 'X' to exit.")
        print("Enter 'P' to list all teams from playlists.")
        print("Enter 'C' to add a sports team along with their performance to the playlist.")
        print("Enter 'D' to delete a sports team along with their performance from the playlist.")
        print("Enter 'S' to show a sports team along with their performance from the playlist.")

    @classmethod
    def create_playlist(cls):
        name = input_string("Please enter the name of the NBA team for the playlist: ", "Name must be non-empty.")
        thumbnail = input_string("Please enter the URL for the team's top 5 dunks from last season: ")
        description = input_string("Enter the description for the playlist: ", valid=lambda x: True)

        playlist = PlayList(name, thumbnail, description)
        Database.add_playlist(playlist)

    @classmethod
    def delete_playlist(cls):
        name = input_string("Please enter the name of the playlist you want to delete: ", "Name must be non-empty.")
        Database.delete_playlist(name)

    @classmethod
    def show_playlist(cls):
        name = input_string("Please enter the name of the playlist you want to show: ", "Name must be non-empty.")
        playlist = Database.get_playlist(name)
        if playlist is not None:
            print(playlist)
        else:
            print("Playlist not found.")

    @classmethod
    def list_all_playlists(cls):
        playlists = Database.get_all_playlists()
        if playlists:
            for playlist in playlists:
                print(playlist)
        else:
            print("No playlists available.")

    @classmethod
    def run(cls):
        while True:
            cls.print_menu()
            choice = select_item("Please select an item: ", "Error. Please type in a valid menu choice.",
                                 ['L', 'X', 'P', 'C', 'D', 'S'])
            if choice == "L":
                get_playlists = Database.get_data()
                print(get_playlists)
                if get_playlists:
                    for data in get_playlists:
                        print(data)
                else:
                    print("No sports team performance data available.")
            elif choice == "P":
                cls.list_all_playlists()
            elif choice == "C":
                cls.create_playlist()
            elif choice == "D":
                cls.delete_playlist()
            elif choice == "S":
                cls.show_playlist()
            elif choice == "X":
                break


if __name__ == "__main__":
    ConsoleUI.run()



