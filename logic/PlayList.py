class PlayList:
    __name = ""
    __videos = []
    __thumbnail = ""
    __description = ""
    __map = {}

    def __init__(self, name, thumbnail, description):
        self.name = name
        self.thumbnail = thumbnail
        self.description = description

    def __str__(self):
        return f"Name: {self.name}\nThumbnail: {self.thumbnail}\nDescription: {self.description}"

    def get_key(self):
        return self.__name.lower()

    @classmethod
    def get_name(cls, name):
        return name.lower()

    @classmethod
    def lookup(cls, key):
        if key in cls.__map:
            return cls.__map[key.lower]
        else:
            return None

    @classmethod
    def get_playlists(cls):
        from data.Database import Database

        return Database.get_data()
