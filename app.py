# app.py
from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")  # this page extends base.html

@app.route("/projects")
def projects():
    return render_template("projects.html")

@app.route("/apps")
def apps():
    return render_template("apps.html")

@app.route("/data-projects")
def data_projects():        # endpoint name = data_projects  ✅
    return render_template("data_projects.html")  # file name must match exactly

@app.route("/contact")
def contact():              # endpoint name = contact        ✅
    return render_template("contact.html")

@app.route("/resume")
def resume():
    return render_template("resume.html")
