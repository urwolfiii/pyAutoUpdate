import subprocess

import flask

app = flask.Flask(__name__)
global port
port = 123456


@app.route("/get_update_info/")
def get_update_info():
    return flask.send_file("./update/auto_update_version.txt")


@app.route("/install_update/")
def install_update():
    return flask.send_file("./update/update.zip")


app.run(host="127.0.0.1", port=port)
