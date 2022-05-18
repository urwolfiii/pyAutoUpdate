#!/usr/bin/env python3

import flask, os


app = flask.Flask(__name__)
PORT = 123456


@app.route("/get_update_info/<version>")
def get_update_info(version: str = "stable"):
    print(f"./{version}/auto_update_version.txt")
    if os.path.exists(version):
        return flask.send_file(f"./{version}/auto_update_version.txt")
    return flask.send_file(f"./stable/auto_update_version.txt")


@app.route("/install_update/<version>")
def install_update(version: str = "stable"):
    print(f"./{version}/auto_update_version.txt")
    if os.path.exists(version):
        return flask.send_file(f"./{version}/update.zip")
    return flask.send_file(f"./stable/update.zip")


app.run(host="127.0.0.1", port=PORT)
