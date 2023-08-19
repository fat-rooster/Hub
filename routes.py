from flask import render_template
from . import hub

@hub.route('/')
def hub():
    return render_template('hub.html')