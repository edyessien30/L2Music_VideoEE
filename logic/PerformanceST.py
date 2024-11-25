from logic.SportsTeam import SportsTeam


class PerformanceST(SportsTeam):
    __current_record = ""

    def __init__(self, team_name, location, url, year_of_establishment, current_record,):
        self.__current_record = current_record
        self.__type = "PerformanceST"
        super().__init__(team_name, location, url, year_of_establishment,)

    def to_dict(self):
        dict = super().to_dict()  # More code from week 5, I would like have dict look up in a similar way to marc
        dict["type"] = self.__type
        dict["current_record"] = self.__current_record
        return dict

    def get_key(self):
        return f"{self.get_name()}: {self.get_location()}  {self.get_url()}  {self.__current_record}".lower()

    @staticmethod
    def make_key(team_name, location, url, current_record):
        return f"{team_name}: {location} {url}  {current_record}".lower()

    def __str__(self):
        string = super().__str__()
        return (f"{string}"
                f"{self.__current_record}")
