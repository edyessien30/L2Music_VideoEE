class PlayList:
    ALL_VIDEOS = "All Videos"
    __name = ""
    __videos = []
    __thumbnail = ""
    __description = ""
    __map = {}

    def __init__(self, name, videos, thumbnail, description):
        self.__name = name
        self.__videos = videos
        self.__thumbnail = thumbnail
        self.__description = description
        self.__class__.__map[self.get_key()] = self

    def to_dict(self):
        return {
            "_id": self.get_key(),
            "name": self.__name,
            "thumbnail": self.__thumbnail,
            "description": self.__description,
            "videos": [video.get_key() for video in self.__videos]
        }

    def get_key(self):
        return self.__name.lower()

    def get_name(self):
        return self.__name

    def get_thumbnail(self):
        return self.__thumbnail

    def get_description(self):
        return self.__description

    @classmethod
    def lookup(cls, key):
        lower_key = key.lower()
        if lower_key in cls.__map:
            return cls.__map[lower_key]
        else:
            return None

    def append(self, video):
        self.__videos.append(video)

    def remove(self, video):
        self.__videos.remove(video)

    def delete(self):
        del self.__class__.__map[self.get_key()]

    def __iter__(self):
        return self.__videos.__iter__()

    def __contains__(self, video):
        return video in self.__videos

    def __add__(self, other):
        name = f"{self.get_name()}/{other.get_name()}"
        thumbnail = self.get_thumbnail()
        description = self.get_description() + " " + other.get_description()
        new_playlist = PlayList(name, [], thumbnail, description)
        for video in self:
            if video not in new_playlist:
                new_playlist.append(video)
        for video in other:
            if video not in new_playlist:
                new_playlist.append(video)
        return new_playlist

    @staticmethod
    def get_playlists():
        from data.Database import Database

        return Database.get_playlists()

    @staticmethod
    def rebuild_data():
        from data.Database import Database

        return Database.rebuild_data()
