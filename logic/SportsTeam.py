class SportsTeam:
    __team_name = ""
    __location = ""
    __url = ""
    __year_of_establishment = 0
    __note = ""
    __map = {}

    def __init__(self, team_name, location, url, year_of_establishment, note):
        self.__team_name = team_name
        self.__location = location
        self.__url = url
        self.__year_of_establishment = year_of_establishment
        self.__note = note
        self.__class__.__map[self.get_key()] = self

    def get_key(self):
        return f"{self.__team_name}: {self.__location}".lower()

    def __str__(self):
        return f"{self.__team_name}: {self.__url}"

    def get_location(self):
        return self.__location

    def get_year_of_establishment(self):
        return self.__year_of_establishment

    def get_name(self):
        return self.__team_name

    def delete(self):
        from data.Database import Database
        del self.__class__.__map[self.get_key()]
        Database.delete_team(self)


