from logic.SportsTeam import SportsTeam
from logic.PerformanceST import PerformanceST
from logic.PlayList import PlayList


class Database:
    @staticmethod
    def get_data() -> object:
        p_tb = PerformanceST(
            "Portland Trail Blazers",
            "Top 5 Dunks of the 2023-2024 Season",
            "https://www.youtube.com/watch?v=RWTxnliPxnE&t=26s",
            "Top 5 Dunks of the 2023-2024 Season | Portland Trail Blazers - YouTube",
            "Proud Fan of the Trailblazers",
            ""
        )

        lakers = PerformanceST(
            "Los Angeles Lakers",
            "Top 5 Dunks of the 2023-2024 Season",
            "https://www.youtube.com/watch?v=lakers_dunks",
            "Top 5 Dunks of the 2023-2024 Season | Los Angeles Lakers - YouTube",
            "Proud Fan of the Lakers",
            ""
        )

        clippers = PerformanceST(
            "Los Angeles Clippers",
            "Top 5 Dunks of the 2023-2024 Season",
            "https://www.youtube.com/watch?v=clippers_dunks",
            "Top 5 Dunks of the 2023-2024 Season | Los Angeles Clippers - YouTube",
            "Proud Fan of the Clippers",
            ""
        )

        warriors = PerformanceST(
            "Golden State Warriors",
            "Top 5 Dunks of the 2023-2024 Season",
            "https://www.youtube.com/watch?v=warriors_dunks",
            "Top 5 Dunks of the 2023-2024 Season | Golden State Warriors - YouTube",
            "Proud Fan of the Warriors",
            ""
        )

        kings = PerformanceST(
            "Sacramento Kings",
            "Top 5 Dunks of the 2023-2024 Season",
            "https://www.youtube.com/watch?v=kings_dunks",
            "Top 5 Dunks of the 2023-2024 Season | Sacramento Kings - YouTube",
            "Proud Fan of the Kings",
            ""
        )

        return [p_tb, lakers, clippers, warriors, kings]

    playlists = []

    @classmethod
    def add_playlist(cls, playlist):
        cls.playlists.append(playlist)

    @classmethod
    def delete_playlist(cls, name):
        for playlist in cls.playlists:
            if playlist.name == name:
                cls.playlists.remove(playlist)
                break

    @classmethod
    def get_playlist(cls, name):
        for playlist in cls.playlists:
            if playlist.name == name:
                return playlist
        return None

    @classmethod
    def get_all_playlists(cls):
        return cls.playlists


if __name__ == "__main__":
    videos = Database.get_data()
    for video in videos:
        print(video.get_key(), ": ", video, sep="")
