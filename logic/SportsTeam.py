class SportsTeam:
    __team_name = ""
    __location = ""
    __url = ""
    __year_of_establishment = 0
    __type = ""
    __map = {}

    def __init__(self, team_name, location, url, year_of_establishment, save=False):
        self.__team_name = team_name
        self.__location = location
        self.__url = url
        self.__year_of_establishment = year_of_establishment
        self.__type = "SportsTeam"
        self.__class__.__map[self.get_key()] = self
        if save:
            self.save()

    @classmethod
    def build(cls, team_dict):
        from logic.PerformanceST import PerformanceST
        if team_dict["type"] == "SportsTeam":
            return SportsTeam(
                team_dict["team_name"],
                team_dict["location"],
                team_dict["url"],
                team_dict["year_of_establishment"],
                team_dict["type"],

            )
        elif team_dict["type"] == "PerformanceST":
            return PerformanceST(
                team_dict["team_name"],
                team_dict["location"],
                team_dict["url"],
                team_dict["year_of_establishment"],
                team_dict["current_record"],
            )

    def to_dict(self):
        return {
            "_id": self.get_key(),  # I commented the get key method out for the sake of running the class method rd
            "team_name": self.__team_name,
            "location": self.__location,
            "url": self.__url,  # this is the dictionary
            "year_of_establishment": self.__year_of_establishment,  # another edition to part 1 of Databases
            "type": self.__type
        }

    def get_id(self):
        return f"{self.get_key()}|{self.__url}"

    def get_key(self):
        return f"{self.__team_name}: {self.__location}".lower()

    @staticmethod
    def make_key(team_name, location):
        return f"{team_name}: {location}".lower()  # Lab 6 addition

    def __str__(self):
        return f"{self.__team_name}: {self.__url}"

    def get_location(self):
        return self.__location

    def update_team(self, team_name):
        self.__team_name = team_name  # method to update teams from marc video "Setter"
        self.save()

    def get_year_of_establishment(self):
        return self.__year_of_establishment

    def get_name(self):
        return self.__team_name

    def get_url(self):
        return self.__url

    def delete(self):
        from data.Database import Database
        del self.__class__.__map[self.get_key()]
        Database.delete_team(self)

    def save(self):
        from data.Database import Database

        Database.save_team(self)

    @classmethod
    def lookup(cls, key):
        if key in cls.__map:
            return cls.__map[key]
        else:
            return None

            #   MAp contains sportsteam object but when I look the key it's getting a string vs a PST instance


