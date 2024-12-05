from flask import Flask, render_template, request
from logic.Conference import Conference
from logic.SportsTeam import SportsTeam


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
            "add_team": "Create a new team.",
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
            "show_playlist": "Show a conference.",
        }
    }

    @staticmethod
    @__app.route('/')
    @__app.route('/index')
    @__app.route('/index.html')
    @__app.route('/index.php')
    def homepage():
        return render_template('homepage.html', options=WebUI.MENU)  # return render_template("homepage.html", options=WebUI.MENU)

    @classmethod
    def init(cls):
        cls.__all_teams, cls.__all_conferences = Conference.read_data()



    @staticmethod
    @__app.route('/list_all_conferences')
    def list_conferences():
        return render_template("list/list_conferences.html", conferences=WebUI.__all_conferences)


    @staticmethod
    @__app.route('/list_conference')
    def list_conference():
        if "conference" not in request.args:
            return render_template(
                "error.html",
                message_header="Conference not specified!",
                message_body="No conference was specified. Please check the URL and try again."
            )
        key = request.args["conference"]
        conference = Conference.lookup(key)
        if conference is None:
            return render_template(
                "error.html",
                message_header="Conference not found!",
                message_body=f"The Conference named '{key}' was not found. Please check the URL and try again."
            )
        return render_template("list/list_conference.html", conference=conference)

    @classmethod
    def run(cls):
        cls.__app.run(port=8000)


if __name__ == '__main__':
    WebUI.init()
    WebUI.run()

