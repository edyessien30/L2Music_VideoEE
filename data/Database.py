from logic.SportsTeam import SportsTeam
from logic.PerformanceST import PerformanceST
from logic.Conference import Conference
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

class Database:
    PASSWORD = "Eessie112430!"
    USERNAME = "edyessien"
    CLUSTER = "@cluster0.omcmt.mongodb.net"
    __connection = None
    __database = None
    __teams__collection = None
    __conference__colletion = None
    URI = f"mongodb+srv://{USERNAME}:{PASSWORD}{CLUSTER}/?retryWrites=true&w=majority&appName=Cluster0"
    all_conference = None
    @classmethod
    def connect(cls):
        if cls.__connection is None:
            cls.__connection = MongoClient(cls.URI, server_api=ServerApi('1'))
            cls.__database = cls.__connection.SportsTeams
            cls.__teams__collection = cls.__database.Teams
            cls.__conference__colletion = cls.__database.Conference

            print("Client:", cls.__connection)
            print("Database:", cls.__database)
            print("Client:", cls.__teams__collection)
            print("Client:", cls.__conference__colletion)

    @staticmethod
    def get_data():
        p_tb = PerformanceST(
            "Portland Trail Blazers",
            "Top 5 Dunks of the 2023-2024 Season",
            "https://www.youtube.com/watch?v=RWTxnliPxnE&t=26s",
            "Top 5 Dunks of the 2023-2024 Season | Portland Trail Blazers - YouTube",
            "Proud Fan of the Trailblazers",
            ""
        )

        lakers = PerformanceST(
            "Los Angeles Lakers",
            "Top 5 Dunks of the 2023-2024 Season",
            "https://www.youtube.com/watch?v=lakers_dunks",
            "Top 5 Dunks of the 2023-2024 Season | Los Angeles Lakers - YouTube",
            "Proud Fan of the Lakers",
            ""
        )

        clippers = PerformanceST(
            "Los Angeles Clippers",
            "Top 5 Dunks of the 2023-2024 Season",
            "https://www.youtube.com/watch?v=clippers_dunks",
            "Top 5 Dunks of the 2023-2024 Season | Los Angeles Clippers - YouTube",
            "Proud Fan of the Clippers",
            ""
        )

        warriors = PerformanceST(
            "Golden State Warriors",
            "Top 5 Dunks of the 2023-2024 Season",
            "https://www.youtube.com/watch?v=warriors_dunks",
            "Top 5 Dunks of the 2023-2024 Season | Golden State Warriors - YouTube",
            "Proud Fan of the Warriors",
            ""
        )

        kings = PerformanceST(
            "Sacramento Kings",
            "Top 5 Dunks of the 2023-2024 Season",
            "https://www.youtube.com/watch?v=kings_dunks",
            "Top 5 Dunks of the 2023-2024 Season | Sacramento Kings - YouTube",
            "Proud Fan of the Kings",
            ""
        )
        memphis = PerformanceST(
            "Memphis Grizzlies",
            "Top 5 Dunks of the 2023-2024 Season",
            "https://www.youtube.com/watch?v=kings_dunks",
            "Top 5 Dunks of the 2023-2024 Season | Sacramento Kings - YouTube",
            "Proud Fan of the Grizzlies",
            ""
        )
        thunder = PerformanceST(
            "Oklahoma City Thunder",
            "Top 5 Dunks of the 2023-2024 Season",
            "https://www.youtube.com/watch?v=kings_dunks",
            "Top 5 Dunks of the 2023-2024 Season | Sacramento Kings - YouTube",
            "Proud Fan of the Thunder",
            ""
        )
        nuggets = PerformanceST(
            "Denver Nuggets",
            "Top 5 Dunks of the 2023-2024 Season",
            "https://www.youtube.com/watch?v=kings_dunks",
            "Top 5 Dunks of the 2023-2024 Season | Sacramento Kings - YouTube",
            "Proud Fan of the Nuggets",
            ""
        )
        timberwolves = PerformanceST(
            "Minnesota Timberwolves",
            "Top 5 Dunks of the 2023-2024 Season",
            "https://www.youtube.com/watch?v=kings_dunks",
            "Top 5 Dunks of the 2023-2024 Season | Sacramento Kings - YouTube",
            "Proud Fan of the Timberwolves",
            ""
        )
        spurs = PerformanceST(
            "San Antonio Spurs",
            "Top 5 Dunks of the 2023-2024 Season",
            "https://www.youtube.com/watch?v=kings_dunks",
            "Top 5 Dunks of the 2023-2024 Season | Sacramento Kings - YouTube",
            "Proud Fan of the Spurs",
            ""
        )
        jazz = PerformanceST(
            "Utah Jazz",
            "Top 5 Dunks of the 2023-2024 Season",
            "https://www.youtube.com/watch?v=kings_dunks",
            "Top 5 Dunks of the 2023-2024 Season | Sacramento Kings - YouTube",
            "Proud Fan of the Jazz",
            ""
        )
        suns = PerformanceST(
            "Phoenix Suns",
            "Top 5 Dunks of the 2023-2024 Season",
            "https://www.youtube.com/watch?v=kings_dunks",
            "Top 5 Dunks of the 2023-2024 Season | Sacramento Kings - YouTube",
            "Proud Fan of the Suns",
            ""
        )
        #The following section is about conferences.
        Western_Conference = Conference(
            name="Western Conference",
            thumbnail="top 5 dunks",
            description="team from the western confernece",
            teams=[p_tb, lakers, clippers, warriors, kings, memphis, thunder, nuggets, timberwolves, spurs, jazz, suns])

        Eastern_Conference = Conference(
            name="Eastern Conference",
            thumbnail="top 5 dunks",
            description="team from the western confernece",
            teams=[])

        all_conference = Conference(
            name="all",
            thumbnail="top 5 dunks",
            description="team from all the western confernece",
            teams=[p_tb, lakers, clippers, warriors, kings, memphis, thunder, nuggets, timberwolves, spurs, jazz, suns])
        # We just built all the teams along with their conferences.
        # In this case we will be returning all_conferences = all teams and a list of conferences
        return all_conference, [Western_Conference, Eastern_Conference, all_conference]

    @classmethod
    def rebuild_data(cls):
        cls.connect()
        cls.__teams__collection.drop()              #157-160 Remake both collections
        cls.__teams__collection = cls.__database.Teams
        cls.__conference__colletion.drop()
        cls.__conference__colletion = cls.__database.Conference

        all_teams, all_conferences = cls.get_data()

        team_dicts = [team.to_dict() for team in all_teams]
        cls.__teams__collection.insert_many(team_dicts)

        conference_dicts = [conference.to_dict() for conference in all_conferences]
        cls.__conference__colletion.insert_many(conference_dicts)



     #   for team in all_teams:
     #       print(team)                            # New addition to week 5 project Along with pymong connection above

    @classmethod
    def add_playlist(cls, playlist):
        cls.playlists.append(playlist)

    @classmethod
    def delete_team(cls, team_name):
        for team in cls.get_data()[0]:
            if team.get_name() == team_name:
                team.remove(team_name)
                break

    @classmethod
    def delete_playlist(cls, name):
        for playlist in cls.playlists:
            if playlist.name == name:
                cls.playlists.remove(playlist)
                break

    @classmethod
    def get_playlist(cls, name):
        for playlist in cls.playlists:
            if playlist.lower() == name.lower():
                return playlist
            return None

    @classmethod
    def get_all_playlists(cls):
        return cls.playlists


    playlists = []
    name = ""


if __name__ == "__main__":
    all_teams, all_conferences = Database.get_data()
    print(all_teams)
    print("the following is going to print all_teams with iterable and get_key.")
    for team in all_teams:
        print(team.get_key())
    print("The following is going to print all_teams with get_teams without get_key.")
    for team in all_teams.get_teams():
        print(team)
    print(all_teams.get_key()) # This produces no errors because we worked on the defined conference class and defined it's get key method.
