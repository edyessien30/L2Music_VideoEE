from logic.SportsTeam import SportsTeam


class PerformanceST(SportsTeam):
    __current_record = ""

    def __init__(self, team_name, location, year_of_establishment, note, current_record):
        super().__init__(team_name, location, year_of_establishment, note)
        self.__current_record = current_record

