from logic.SportsTeam import SportsTeam
from ui.WebUI import WebUI
from flask import render_template, request
from logic.Conference import Conference
from logic.PerformanceST import PerformanceST  # because of "Current_record" in sports teams


class CreateRoutes(WebUI):
    __app = WebUI.get_app()

    @staticmethod
    @__app.route('/create_conference')
    def create_conference():
        return render_template("create/create_conference.html")

    @staticmethod
    @__app.route('/do_create_conference', methods=['GET', 'POST'])
    def do_create_conference():
        if "name" not in request.form:
            return render_template(
                "error.html",
                message_header="Conference name not specified!",
                message_body="No conference name was specified. Please check form and try again."
            )
        name = request.form["name"]
        key = request.form["name"].lower()
        conference = Conference.lookup(key)
        if conference is not None:
            return render_template(
                "error.html",
                message_header="Conference already exists!",
                message_body=f"A Conference named {name} already exists. Please choose another name and try again."
            )
        key = name.lower()
        conference = Conference.lookup(key)
        if conference is not None:
            return render_template(
                "error.html",
                message_header="Conference already exists!",
                message_body=f"A conference name {name} already exists. Please check choose another name and try again."
            )
        if "description" in request.form:
            description = request.form["description"].strip()
        else:
            description = ""
        if "teams" in request.form:
            team_name = request.form["teams"].strip()
            team = WebUI.get_team_by_name(team_name)
            teams = []
            if team is not None:
                teams.append(team)
                team.save()
        else:
            teams = ""
        conference = Conference(name, [], description, teams, save=True)
        WebUI.get_all_conferences().append(conference)
        return render_template("create/confirm_conference_created.html", conference=conference)

    @staticmethod
    @__app.route('/create_sports_team')
    def create_sports_team():
        return render_template("create/create_sports_team.html")

    @staticmethod
    @__app.route('/do_create_sports_team', methods=['GET', 'POST'])
    def do_create_sports_team():
        # team_name, location, url, year_of_establishment, current_record
        if "team_name" not in request.form:
            return render_template(
                "error.html",
                message_header="Sports Team name not specified!",
                message_body="No Sports team name was specified. Please check form and try again."
            )
        team_name = request.form["team_name"]
        key = request.form["team_name"].lower()
        sports_team = SportsTeam.lookup(key)
        if sports_team is not None:
            return render_template(
                "error.html",
                message_header="Sports Team already exists!",
                message_body=f"A Sports Team name {team_name} already exists. Please choose another name and try again."
            )
        if "location" not in request.form:
            return render_template(
                "error.html",
                message_header="Sports team name not specified!",
                message_body="No Sports team name was specified. Please check form and try again."
            )
        location = request.form["location"]
        key = request.form["location"].lower()
        sports_team = SportsTeam.lookup(key)
        if sports_team is not None:
            return render_template(
                "error.html",
                message_header="Sports Team already exists!",
                message_body=f"A Sports Team name {location} already exists. Please choose another name and try again."
            )
        if "location" in request.form:
            location = request.form["location"].strip()
        else:
            location = ""
        if "url" in request.form:
            url = request.form["url"].strip()
        else:
            url = ""
        if "year_of_establishment" in request.form:
            year_of_establishment = request.form["year_of_establishment"].strip()
        else:
            year_of_establishment = ""
        sports_team = SportsTeam(team_name, location, url, year_of_establishment, save=True)
        WebUI.get_all_teams().append(sports_team)
        return render_template("create/confirm_sports_team_created.html", sports_team=sports_team)
