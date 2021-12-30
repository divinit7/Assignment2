import os

import pandas as pd
from flask import Flask, redirect, render_template, request
from flask.helpers import url_for

app = Flask(__name__, static_folder="./frontend/static")

UPLOAD_FOLDER = "./files"

@app.route("/")
def main():
    return render_template("index.html")

@app.route("/success", methods=['POST'])
def uploadFiles():
    file = request.files['file']
    if file.filename!= '':
        file_path = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(file_path)
    return render_template("success.html", name=file.filename)

if __name__=='__main__':
    app.run(debug=True)
