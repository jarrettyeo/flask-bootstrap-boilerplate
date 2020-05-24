from flask import render_template, flash

from app import app

@app.route('/')
def index():
    msg = "Flashes a message to the next request. In order to remove the flashed message from the session and to display it to the user, the template has to call get_flashed_messages. :param message: the message to be flashed. :param category: the category for the message. The following values are recommended: 'message' for any kind of message"
    flash(msg, "info")
    flash(msg, "info")
    flash(msg, "info")
    return render_template('index.html')

@app.route('/upload')
def upload():
    msg = "Flashes a message to the next request. In order to remove the flashed message from the session and to display it to the user, the template has to call get_flashed_messages. :param message: the message to be flashed. :param category: the category for the message. The following values are recommended: 'message' for any kind of message"
    flash(msg, "success")
    flash(msg, "success")
    flash(msg, "success")
    return render_template('upload.html')