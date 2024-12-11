from ui.WebUI import WebUI
from flask import render_template, request
from logic.Conference import Conference


class ListRoutes:
    __app = WebUI.get_app()

    @staticmethod
    @__app.route('/list_all_conferences')
    def list_conferences():
        return render_template("list/list_conferences.html", conferences=WebUI.get_all_conferences())

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
