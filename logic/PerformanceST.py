from logic.SportsTeam import SportsTeam


class PerformanceST(SportsTeam):
    __current_record = ""

    def __init__(self, team_name, location, url, year_of_establishment, note, current_record):
        super().__init__(team_name, location, url, year_of_establishment, note)
        self.__current_record = current_record

    def to_dict(self):
        dict = super().to_dict()      # More code from week 5, I would like have dict look up in a similar way to marc
        return dict

    def __str__(self):
        string = super().__str__()
        return (f"{string}"
                f"{self.__current_record}")
