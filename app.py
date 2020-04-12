from flask import Flask, render_template
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.config["SECRET_KEY"] = "SECRET"
debug = DebugToolbarExtension(app)


@app.route('/')
def home():
    return render_template("base.html")