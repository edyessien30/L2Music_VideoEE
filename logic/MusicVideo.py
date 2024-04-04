class MusicVideo:
    __artist = ""
    __title = ""
    __url = ""
    __release_year = 0
    __note = ""
    __map = {}

    def __init__(self, artist, title, url, year, note):
        self.__artist = artist
        self.__title = title
        self.__url = url
        self.__year = year
        self.__note = note
        self.__class__.__map[self.get_key()] = self

    def get_key(self):
        return f"{self.__artist}: {self.__title}".lower()

    def get_artist(self):
        return self.__artist

    def get_title(self):
        return self.__title

    def __str__(self):
        return f"<{self.__title} by {self.__artist}: {self.__url}>"

    @staticmethod
    def get_videos():
        from data.Database import Database

        return Database.get_videos()
