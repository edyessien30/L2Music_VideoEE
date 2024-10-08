from logic.SportsTeam import SportsTeam
from logic.PerformanceST import PerformanceST
from logic.PlayList import PlayList

class Database:
    @staticmethod
    def get_data():
        p_tb = PerformanceST(
            "Portland Trail Blazers",
            "Top 5 Dunks of the 2023-2024 Season",
            "https://www.youtube.com/watch?v=RWTxnliPxnE&t=26s",
            "Top 5 Dunks of the 2023-2024 Season | Portland Trail Blazers - YouTube",
            "Proud Fan of the Trailblazers",
            ""
        )

        
        return [p_tb]


if __name__ == "__main__":
    videos = Database.get_data()
    for video in videos:
        print(video.get_key(), ": ", video, sep="")
