from logic.MusicVideo import MusicVideo


class PerformanceVideo(MusicVideo):
    __location = ""
    __performance_date = ""

    def __init__(self, artist, title, url, year, note, location, performance_date):
        self.__location = location
        self.__performance_date = performance_date
        super().__init__(artist, title, url, year, note)

    def get_key(self):
        return f"{self.get_artist()}: {self.get_title()} at {self.__location} on {self.__performance_date}".lower()

    @staticmethod
    def make_key(artist, title, location, performance_date):
        return f"{artist}: {title} at {location} on {performance_date}".lower()
