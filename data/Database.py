from logic.MusicVideo import MusicVideo
from logic.PerformanceVideo import PerformanceVideo

class Database:
    @staticmethod
    def get_videos():
        bs_bbl = MusicVideo("Bruce Springsteen", "Blinded by the Light",
                            "https://www.youtube.com/watch?v=xPy82OO6vRg", 1973, "The original version")
        mm_bbl = MusicVideo("Manfred Mann's Earth Band", "Blinded by the Light",
                            "https://www.youtube.com/watch?v=Rzk3x3HZbJI", 1976,
                            "Cover version of a song by Bruce Springsteen")
        bs_btn = PerformanceVideo("Bruce Springsteen", "Because the Night",
                                  "https://www.youtube.com/watch?v=-Evp0MrJ9lk", 1978,
                                  "Written by Bruce and Patti Smith", "Houston", "1978")
        ps_btn = MusicVideo("Patti Smith", "Because the Night",
                            "https://www.youtube.com/watch?v=c_BcivBprM0", 1978,
                            "Written by Bruce and Patti")
        return [bs_bbl, mm_bbl, bs_btn, ps_btn]


if __name__ == "__main__":
    videos = Database.get_videos()
    for video in videos:
        print(video.get_key(), ": ", video, sep="")
