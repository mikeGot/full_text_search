from flask import Flask, url_for
from flask import send_from_directory, redirect, render_template, request
import urllib.parse

import config
from string_processing import preparing_to_search
app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def base_page():
    if request.method == 'GET':
        return render_template('index.html')
    elif request.method == 'POST':
        print(request.form.to_dict())
        return redirect(url_for("results",
                                name=request.form["text"],
                                chosen_operator=request.form["operator"],
                                number_of_results=int(request.form["number_of_results"])))


@app.route("/results/<name>+<chosen_operator>+<number_of_results>", methods=['GET', 'POST'])
def results(name: str, chosen_operator: str, number_of_results: int):
    if request.method == "GET":
        return preparing_to_search(name)


if __name__ == "__main__":
    app.run(debug=True)
