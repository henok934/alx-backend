#!/usr/bin/env python3
"""
Module 0-app
"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    """create index method for retrieve the index value"""
    return render_template("0-index.html")


if __name__ == "__main__":
    app.run(debug=True)
