from ui.WebUI import WebUI
from flask import render_template, request
from logic.Conference import Conference
from logic.SportsTeam import SportsTeam


class DeleteRoutes:
    __app = WebUI.get_app()

    @staticmethod
    @__app.route("/delete_conference")
    def delete_conference():
        return render_template("delete/delete_conference.html", conferneces=WebUI.get_all_conferences())

    @staticmethod
    @__app.route("/do_delete_conference", methods=["GET", "POST"])
    def do_delete_conference():
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
                message_header="Conference name does not exists!",
                message_body=f"A Conference named {name} does not exist. Please choose another name and try again."
            )
        WebUI.get_all_conferences().remove(conference)
        # Conference.delete()
        return render_template("delete/confirm_conference_deleted.html", conference=conference)

    @staticmethod
    @__app.route("/delete_team")
    def delete_team():
        return render_template("delete/delete_team.html", teams=WebUI.get_all_teams())

    @staticmethod
    @__app.route("/do_delete_team", methods=["GET", "POST"])
    def do_delete_team():
        if "team_name" not in request.form:
            return render_template(
                "error.html",
                message_header="Sports Team name not specified!",
                message_body="No Sports Team name was specified. Please check form and try again."
            )
        if "location" not in request.form:
            return render_template(
                "error.html",
                message_header="Sports Team name not specified!",
                message_body="No Sports Team name was specified. Please check form and try again."
            )
        team_name = request.form["team_name"]
        location = request.form["location"]
        key = f"{team_name}: {location}".lower()
        sports_team = SportsTeam.lookup(key)
        if sports_team is None:
            return render_template(
                "error.html",
                message_header="Sports team name does not exists!",
                message_body=f"A Sports team named {team_name} does not exist. Please choose another name and try again."
            )
        WebUI.get_all_teams().remove(sports_team)
        return render_template("delete/confirm_sports_team_deleted.html", sports_team=sports_team)
