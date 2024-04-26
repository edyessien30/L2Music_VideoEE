from logic.SportsTeam import SportsTeam


class PermissionST(SportsTeam):
    __current_record = ""

    def __init__(self, team_name, location, year_of_establishment, note, current_record):
        super().__init__(team_name, location, year_of_establishment, note)
        self.__current_record = current_record

    @property
    def get_key(self):
        return (f"{self.__team_name}: {self.__location} on {self.__year_of_establishment} is {self.__current_record}"
                .lower())
