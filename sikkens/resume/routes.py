
from flask import Blueprint,render_template

resume  = Blueprint('resume',__name__)

@resume.route('/')
def index():
    return render_template("index.html")
