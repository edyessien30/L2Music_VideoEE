class SportsTeam:
    __team_name = ""
    __location = ""
    __year_of_establishment = 0
    __note = ""
    __map = {}

    def __init__(self, team_name, location, year_of_establishment, note):
        self.__team_name = team_name
        self.__location = location
        self.__year_of_establishment = year_of_establishment
        self.__note = note
        self.__class__.__map[self.get_key()] = self

    def get_key(self):
        return f"{self.__team_name}: {self.__location}".lower()
