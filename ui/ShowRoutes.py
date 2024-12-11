from ui.WebUI import WebUI
from flask import render_template, request
from logic.Conference import Conference


class ShowRoutes(WebUI):
    __app = WebUI.get_app()

    @staticmethod
    @__app.route('/show_conference')
    def show_conference():
        return render_template(
            "show/show_conference.html",
            conference=WebUI.get_all_conferences()
        )

    @staticmethod
    @__app.route("/do_show_conference", methods=['GET', 'POST'])
    def do_show_conference():
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
        for conference in WebUI.get_all_conferences():
            if conference.get_name() == name.lower():
                print(conference)
        return render_template("show/confirm_conference_shown.html", conference=conference)
