from logic.SportsTeam import SportsTeam
from ui.WebUI import WebUI
from flask import render_template, request
from logic.Conference import Conference


class JoinRoutes(WebUI):
    __app = WebUI.get_app()

    @staticmethod
    @__app.route("/join_team_con")
    def join_team_con():
        return render_template("join/join_team_con.html", conferences=WebUI.get_all_conferences())

    @staticmethod
    @__app.route("/do_join_team_con", methods=['GET', 'POST'])
    def do_join_team_con():
        if "name" not in request.form:
            return render_template(
                "error.html",
                message_header="Conference name not specified!",
                message_body="No conference name was specified. Please check form and try again."
            )
        name = request.form["name"]
        key = request.form["name"].lower()
        conference = Conference.lookup(key)
        if conference is None:
            return render_template(
                "error.html",
                message_header="Conference doesn't exists!",
                message_body=f"A Conference named {name} doesn't exists. Please choose another name and try again."
            )
        if "team_name" not in request.form:
            return render_template(
                "error.html",
                message_header="Sports Team name not specified!",
                message_body="No Sports team name was specified. Please check form and try again."
            )
        if "location" not in request.form:
            return render_template(
                "error.html",
                message_header="Sports Team location not specified!",
                message_body="No Sports Team location was specified. Please check form and try again."
            )
        team_name = request.form["team_name"]
        location = request.form["location"]
        key = f"{team_name}: {location}".lower()
        team = SportsTeam.lookup(key)
        if team is None:
            return render_template(
                "error.html",
                message_header="Sports Team doesn't exists!",
                message_body=f"A Sports Team name {team_name} doesn't exists. Please choose another name and try again."
            )
        if conference and team:  # Check if both conference and team were found
            WebUI.join_team(team, conference)  # Call the join_team method
            return render_template("join/confirm_team_con_joined.html", conference=conference, team=team)
        return render_template(
            "error.html",
            message_header="Sports Team and COn doesn't exists!",
            message_body=f"A Sports Team name {team_name} and COn doesn't exists. "
                         f"Please choose another name and try again."
        )
