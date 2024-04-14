from logic.MusicVideo import MusicVideo
from logic.PerformanceVideo import PerformanceVideo
from logic.PlayList import PlayList
from ui.input_validation import select_item, input_string, y_or_n, input_int


class ConsoleUI:
    __all_videos = None
    __all_playlists = []

    CHOICES = ["pv", "pp", "cp", "dp", "sp", "cv", "dv", "av", "rv", "uv", "jp", "x"]
    @classmethod
    def init(cls):
        cls.__all_videos, cls.__all_playlists = PlayList.get_playlists()

    @classmethod
    def select_playlist(cls, include_all_videos=False):
        names = []
        map = {}
        pos = 1
        for playlist in cls.__all_playlists:
            if include_all_videos or playlist.get_name() != PlayList.ALL_VIDEOS:
                names.append(playlist.get_name())
                map[str(pos)] = playlist.get_name()
                pos += 1
        names.append("None")
        map[str(pos)] = "None"
        print("Please select a playlist name from the list below: ")
        pos = 1
        for name in names:
            print(f"    {pos}: {name}")
            pos += 1
        name = select_item("Enter the name or 'None' to exit: ", "Please type a playlist name!", choices=names, map=map)
        if name == "None":
            return None
        playlist = PlayList.lookup(name)
        return playlist

    @classmethod
    def select_video(cls, playlist=None):
        if playlist is None:
            playlist = cls.__all_videos
        keys = []
        map = {}
        pos = 1
        for video in playlist:
            keys.append(video.get_key())
            map[str(pos)] = video.get_key()
            pos += 1
        keys.append("None")
        map[str(pos)] = "None"
        print("Please select a video from the list below: ")
        pos = 1
        for key in keys:
            print(f"    {pos}: {key}")
            pos += 1
        key = select_item("Enter the video or 'None' to exit: ", "Please type a video!", choices=keys, map=map)
        if key == "None":
            return None
        video = MusicVideo.lookup(key)
        return video

    @classmethod
    def list_videos(cls):
        for video in cls.__all_videos:
            print(video.get_key(), ": ", video, sep="")

    @classmethod
    def list_playlists(cls):
        for playlist in cls.__all_playlists:
            print(f"{playlist.get_name()}: {playlist.get_description()}")

    @classmethod
    def create_playlist(cls):
        # name, videos, thumbnail, description
        name = input_string("Please enter the name of the playlist or 'None' to exit: ", "Name must be non-empty.")
        if name == "None":
            return
        playlist = PlayList.lookup(name)
        if playlist is not None:
            print("Error! Playlist already exists.")
            return
        thumbnail = input_string("Please enter the URL for the thumbnail image: ", "Name must be non-empty.")
        description = input_string("Please enter a description for the playlist: ", valid=lambda x: True)
        playlist = PlayList(name, [], thumbnail, description)
        cls.__all_playlists.append(playlist)
        print("Playlist created.")

    @classmethod
    def delete_playlist(cls):
        playlist = cls.select_playlist()
        if playlist is None:
            return
        cls.__all_playlists.remove(playlist)
        playlist.delete()
        print("Playlist deleted.")

    @classmethod
    def show_playlist(cls):
        playlist = cls.select_playlist(True)
        if playlist is None:
            return
        print()
        print(f"Name: {playlist.get_name()}")
        print(f"Description: {playlist.get_description()}")
        print(f"Thumbnail: {playlist.get_thumbnail()}")
        print("Videos in the playlist:")
        for video in playlist:
            print("    ", video)

    @classmethod
    def create_video(cls):
        is_performance_video = y_or_n("Is the new video a performance video (y/n): ")
        # artist, title, url, year, note
        artist = input_string("What is the name of the artist: ")
        title = input_string("What is the title of the song: ")
        if not is_performance_video:
            key = MusicVideo.make_key(artist, title)
            video = MusicVideo.lookup(key)
            if video is not None:
                print("The music video already exists!")
                return
        if is_performance_video:
            location = input_string("Where was the song performed: ")
            performance_date = input_string("When was did the performance happen: ")
            key = PerformanceVideo.make_key(artist, title, location, performance_date)
            video = PerformanceVideo.lookup(key)
            if video is not None:
                print("The performance video already exists!")
                return
        url = input_string("What is the URL for the video on YouTube: ")
        year = input_int("What year was the song recorded: ", ge=1000, le=2100)
        note = input_string("Please type a note for the video (or hit return): ", valid=lambda x: True)
        if is_performance_video:
            # location, performance_date
            video = PerformanceVideo(artist, title, url, year, note, location, performance_date)
        else:
            video = MusicVideo(artist, title, url, year, note)
        cls.__all_videos.append(video)
        print("Video created.")

    @classmethod
    def delete_video(cls):
        video = cls.select_video()
        if video is None:
            return
        for playlist in cls.__all_playlists:
            if video in playlist:
                playlist.remove(video)
        video.delete()
        print("Video deleted.")

    @classmethod
    def add_video(cls):
        playlist = cls.select_playlist()
        if playlist is None:
            return
        video = cls.select_video()
        if video is None:
            return
        if video in playlist:
            print("The video is already in the playlist!")
            return
        playlist.append(video)
        print("Added video to playlist.")

    @classmethod
    def remove_video(cls):
        playlist = cls.select_playlist()
        if playlist is None:
            return
        video = cls.select_video(playlist)
        if video is None:
            return
        if video not in playlist:
            print("The video is not in the playlist!")
            return
        playlist.remove(video)
        print("Removed video from playlist.")

    @classmethod
    def update_video(cls):
        video = cls.select_video()
        if video is None:
            return
        note = input_string("Enter the new note: ", valid=lambda x: True)
        video.update_note(note)
        print("Note updated.")

    @classmethod
    def join_playlists(cls):
        playlist_1 = cls.select_playlist(include_all_videos=True)
        if playlist_1 is None:
            return
        playlist_2 = cls.select_playlist(include_all_videos=True)
        if playlist_2 is None:
            return
        new_playlist = playlist_1 + playlist_2
        cls.__all_playlists.append(new_playlist)
        print("Joined playlists.")

    @staticmethod
    def print_menu():
        print("Please select an option from the list below:")
        print("    pv: Print videos")
        print("    pp: Print playlists")
        print("    cp: Create playlist")
        print("    dp: Delete playlist")
        print("    sp: Show playlist")
        print("    cv: Create video")
        print("    dv: Delete video")
        print("    av: Add video to playlist")
        print("    rv: Remove video from playlist")
        print("    uv: Update the note for a video")
        print("    jp: Join two playlists")
        print("    x: Exit")

    @classmethod
    def run(cls):
        while True:
            cls.print_menu()
            choice = select_item("Please select an item: ", "Item must be a choice in the menu.", cls.CHOICES)
            print()
            if choice == "x":
                break
            elif choice == "pv":
                cls.list_videos()
            elif choice == "pp":
                cls.list_playlists()
            elif choice == "cp":
                cls.create_playlist()
            elif choice == "dp":
                cls.delete_playlist()
            elif choice == "sp":
                cls.show_playlist()
            elif choice == "cv":
                cls.create_video()
            elif choice == "dv":
                cls.delete_video()
            elif choice == "av":
                cls.add_video()
            elif choice == "rv":
                cls.remove_video()
            elif choice == "uv":
                cls.update_video()
            elif choice == "jp":
                cls.join_playlists()
            print()
        print("Goodbye!")

if __name__ == "__main__":
    ConsoleUI.init()
    ConsoleUI.run()
