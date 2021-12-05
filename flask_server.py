from flask import Flask, url_for
from flask import send_from_directory, redirect, render_template, request
import urllib.parse

import config

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def base_page():
    if request.method == 'GET':
        return render_template('index.html')
    elif request.method == 'POST':
        return redirect(url_for("success",
                                name=request.form["text"],
                                chosen_operator=request.form["operator"],
                                c_result=request.form["result"]))
