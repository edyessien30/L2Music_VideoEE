class Conference:
    ALL_TEAMS = "all teams"
    __name = ""
    __teams = ""
    __thumbnail = ""
    __description = ""
    __map = {}

    def __init__(self, name, thumbnail, description, teams, save=False):
        self.__name = name
        self.__thumbnail = thumbnail
        self.__description = description
        self.__teams = teams
        self.__class__.__map[self.get_key()] = self
        if save:
            self.save_conference()

    def __iter__(self):
        return iter(self.__teams).__iter__()

    def __str__(self):
        all_team_names = ""
        for name in self.__teams:
            all_team_names += str(name) + " "
        return (f"Name: {self.__name}\nThumbnail: {self.__thumbnail}\nDescription: "  # check read playlist vid for alt
                f"{self.__description}\n"f"Teams: {all_team_names}\n")

    def to_dict(self):
        return {
            "_id": self.get_key(),
            "name": self.__name,  # Another addition to week 5
            "thumbnail": self.__thumbnail,
            "description": self.__description,
            "teams": [team.get_key() for team in self.__teams]

        }

    # def __add__(self, other):
    #     name = f"{self.get_name()}/{other.get_name()}"
    #     thumbnail = self.get_thumbnail()
    #     description = self.get_description() + " " + other.__description()
    #     teams = []
    #     new_conference = Conference(name, thumbnail, description, teams)
    #     for team in self:
    #         if team not in new_conference:
    #             new_conference.append(team, save=False)
    #     for team in other:
    #         if team not in new_conference:
    #             new_conference.append(team, save=False)  # __add__ instance, I noticed in marc video lab 6
    #     new_conference.save()
    #     return new_conference
    # The line of code would be used above if I was joining conferences to conferences in the UI but for the sake of the
    # Context of my lab IN the UI I am joining teams to conferences so the code above is useless unless I change it.

    def get_key(self):
        return self.__name.lower()

    @staticmethod
    def make_key(name):
        return name.lower()

    def get_id(self):
        return f"{self.get_teams()}|{self.__thumbnail}"

    def get_all_conference(self):
        return self.__teams.lower

    def get_teams(self):
        return self.__teams

    def get_thumbnail(self):
        return self.__thumbnail

    def get_description(self):
        return self.__description

    def get_name(self):
        return self.__name.lower()

    def remove(self, team):
        from data.Database import Database
        self.__teams.remove(team)

        Database.save_conference(self)

    def append(self, team, save=True):
        from data.Database import Database

        self.__teams.append(team)  # Lab 6 addition
        if save:
            Database.save_conference(self)

    def delete(self):
        from data.Database import Database

        del self.__class__.__map[self.get_key()]  # Lab 6 addition
        Database.delete_conference(self)

    @classmethod
    def build(cls, conference_dict):
        from logic.SportsTeam import SportsTeam

        return Conference(
            conference_dict["name"],
            conference_dict["thumbnail"],  # another addition to lab 6
            conference_dict["description"],
            # conference_dict["teams"],  #returns team key but the team isn't built
            [SportsTeam.lookup(key) for key in conference_dict["teams"]],  # This line builds the teams.     # "for key"
        )

    @classmethod
    def lookup(cls, key):
        lower_key = key.lower()
        if lower_key in cls.__map:
            return cls.__map[lower_key]
        else:
            return None

    @classmethod
    def get_playlists(cls):
        from data.Database import Database

        return Database.get_data()

    @staticmethod
    def rebuild_data():
        from data.Database import Database

        return Database.rebuild_data()

    @staticmethod
    def read_data():
        from data.Database import Database

        return Database.read_data()

    def save_conference(self):
        from data.Database import Database

        Database.save_conference(self)

    def update_conference(self, name):
        self.__name = name  # method to update conference from marc video "Setter"
        self.save_conference()

    def empty_function(self):
        pass