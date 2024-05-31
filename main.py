from flask import Flask, render_template
import json
from styler import STYLE
app = Flask(__name__)

@app.route('/')
def index():

    return render_template('index.html', s = (STYLE('style.css'))
)


