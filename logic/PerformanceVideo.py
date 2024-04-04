from logic.MusicVideo import MusicVideo


class PerformanceVideo(MusicVideo):
    __location = ""
    __performance_date = ""

    def __init__(self, artist, title, url, year, note, location, performance_date):
        super().__init__(artist, title, url, year, note)
        self.__location = location
        self.__performance_date = performance_date

    def get_key(self):
        return f"{self.get_artist()}: {self.get_title()} at {self.__location} on {self.__performance_date}".lower()
