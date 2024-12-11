from flask import Flask, render_template, request
from logic.Conference import Conference
from logic.PerformanceST import PerformanceST  # because of "Current_record" in sports teams


class WebUI:
    __all_teams = None
    __all_conferences = None
    __app = Flask(__name__, template_folder='templates')
    MENU = {
        "List": {
            "list_conference?conference=All%20Teams": "Print a list of all teams.",
            "list_all_conferences": "Print a list of all conferences.",
        },
        "Create": {
            "create_sports_team": "Create a new team.",
            "create_conference": "Create a new conference.",
        },
        "Join": {
            "join_team_con": "Join a team to a conference.",
        },
        "Delete": {
            "delete_team": "Delete a team.",
            "delete_conference": "Delete a conference."
        },
        "Show": {
            "show_conference": "Show a conference.",
        }
    }

    @staticmethod
    @__app.route('/')
    @__app.route('/index')
    @__app.route('/index.html')
    @__app.route('/index.php')
    def homepage():
        return render_template('homepage.html',
                               options=WebUI.MENU)  # return render_template("homepage.html", options=WebUI.MENU)

    @classmethod
    def init(cls):
        cls.__all_teams, cls.__all_conferences = Conference.read_data()

    @classmethod
    def get_app(cls):
        return cls.__app

    @classmethod
    def get_team_by_name(cls, team_name):
        for team in cls.__all_teams:
            if team.get_name() == team_name:
                return team
        return None

    @classmethod
    def get_all_conferences(cls):
        return cls.__all_conferences

    @classmethod
    def get_all_teams(cls):
        return cls.__all_teams

    @classmethod
    def join_team(cls, team, conference):
        # cls.__all_teams.append(team)
        conference.append(team)
        print(f"{team.get_name()} has been added.")

    @classmethod
    def run(cls):
        from ui.ListRoutes import ListRoutes
        from ui.CreateRoutes import CreateRoutes
        from ui.DeleteRoutes import DeleteRoutes
        from ui.ShowRoutes import ShowRoutes
        from ui.JoinRoutes import JoinRoutes
        cls.__app.run(host="0.0.0.0", port=8000)
