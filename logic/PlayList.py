class PlayList:
    __name = ""
    __videos = []
    __thumbnail = ""
    __description = ""
    __map = {}

    def __init__(self, name, thumbnail, description):
        self.__name = name
        self.__thumbnail = thumbnail
        self.__description = description
        self.__class__.__map[self.get_key()] = self

    def get_key(self):
        return self.__name.lower()

    @classmethod
    def get_key(cls, name):
        return name.lower()

    @classmethod
    def lookup(cls, key):
        if key in cls.__map:
            return cls.__map[key]
        else:
            return None
