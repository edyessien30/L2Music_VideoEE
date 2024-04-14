from logic.MusicVideo import MusicVideo
from logic.PerformanceVideo import PerformanceVideo
from logic.PlayList import PlayList


class Database:
    @classmethod
    def get_playlists(cls):
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

        bs = PlayList("Bruce Springsteen", [bs_bbl, bs_btn],
                      "https://glassgirder.com/music_player/images/bruce.jpg",
                      "The singer/composer Bruce Springsteen")
        ps = PlayList("Patti Smith", [ps_btn],
                      "https://glassgirder.com/music_player/images/patti.jpg",
                      "Patti Smith")
        all = PlayList(PlayList.ALL_VIDEOS, [bs_bbl, mm_bbl, bs_btn, ps_btn],
                       "https://glassgirder.com/music_player/images/all_videos.jpg",
                       "All Videos")

        return all, [bs, ps, all]


if __name__ == "__main__":
    videos = Database.get_videos()
    for video in videos:
        print(video.get_key(), ": ", video, sep="")
