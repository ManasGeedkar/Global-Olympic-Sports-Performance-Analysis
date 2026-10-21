"""
Global Olympic Sports Performance Analysis - Flask Web App
Embeds the Tableau Public dashboards and story into a web UI.
Run:  pip install flask   then   python app.py   ->  open http://127.0.0.1:5000
"""
from flask import Flask, render_template

app = Flask(__name__)

# ---- Tableau Public view URLs (edit here if a link changes) ----
BASE = "https://public.tableau.com/views/GlobalOlympicSportsPerformanceAnalysis/"
VIEWS = {
    "dashboard1": BASE + "GLOBALSPORTSPERFORMANCEANALYTICSDASHBOARD",
    "dashboard2": BASE + "OLYMPICPERFORMANCEANDREGIONALEFFICIENCYDASHBOARD",
    "story":      BASE + "OlympicStory",
}
PROFILE_URL = ("https://public.tableau.com/app/profile/manas.geedkar/viz/"
               "GlobalOlympicSportsPerformanceAnalysis/OlympicStory")


@app.route("/")
def home():
    return render_template("index.html", active="home")


@app.route("/about")
def about():
    return render_template("about.html", active="about")


@app.route("/dashboard")
def dashboard():
    return render_template("viz.html", active="dashboard",
                           title="Global Sports Performance Analytics Dashboard",
                           subtitle="Medals by country, trends over time, sport categories and nation map.",
                           viz_url=VIEWS["dashboard1"], profile=PROFILE_URL)


@app.route("/efficiency")
def efficiency():
    return render_template("viz.html", active="efficiency",
                           title="Olympic Performance & Regional Efficiency Dashboard",
                           subtitle="Regional efficiency, investment vs medals, host-nation advantage.",
                           viz_url=VIEWS["dashboard2"], profile=PROFILE_URL)


@app.route("/story")
def story():
    return render_template("viz.html", active="story",
                           title="Global Olympic Sports Performance Story",
                           subtitle="An 8-scene narrative of Olympic performance from 1992 to 2026.",
                           viz_url=VIEWS["story"], profile=PROFILE_URL)


if __name__ == "__main__":
    app.run(debug=True)
