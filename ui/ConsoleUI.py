from logic.SportsTeam import SportsTeam
from ui.input_validation import select_item
from logic.PlayList import PlayList
from data.Database import Database


class ConsoleUI:
    @staticmethod
    def print_menu():
        print("Select 'L' to list the sports team performance.")
        print("Select 'X' to exit.")
        print("Select 'P' to list all playlists.")


    @classmethod
    def run(cls):
        playlist = PlayList("Playlist Name", "Thumbnail URL", "Playlist Description")
        while True:
            cls.print_menu()
            choice = select_item("Please select an item: ", "Error. Please type in a valid menu choice.", ['L', 'X', 'P'])
            if choice == "L":

                get_playlists = Database.get_data()  # Retrieve sports team performance data from Database.py
                print(get_playlists)
                if get_playlists:
                    for data in get_playlists:
                        print(data)
                else:
                    print("No sports team performance data available.")
            elif choice == "P":
                # Placeholder for listing all playlists
                print("List of all playlists (to be implemented)")
            elif choice == "X":
                break


if __name__ == "__main__":
    ConsoleUI.run()
