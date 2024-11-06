class Conference:
    __name = ""
    __teams = []
    __thumbnail = ""
    __description = ""
    __map = {}

    def __init__(self, name, thumbnail, description, teams):
        self.__name = name
        self.__thumbnail = thumbnail
        self.__description = description
        self.__teams = teams
        self.__class__.__map[self.get_key()] = self

    def __iter__(self):
        return iter(self.__teams)

    def __str__(self):
        all_team_names = ""
        for name in self.__teams:
            all_team_names += str(name) + " "
        return (f"Name: {self.__name}\nThumbnail: {self.__thumbnail}\nDescription: "
                f"{self.__description}\n"f"Teams: {all_team_names}\n")

    def get_key(self):
        return self.__name.lower()

    def get_all_conference(self):
        return self.__teams.lower

    def get_teams(self):
        return self.__teams

    def get_name(self):
        return self.__name.lower()

    def remove(self, team):
        self.__teams.remove(team)

    def add_team(self, team):
        self.__teams.append(team)

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
