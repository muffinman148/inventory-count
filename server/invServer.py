from flask import Flask
from flask import Flask, flash, redirect, render_template, request, session, abort
import os

app = Flask(__name__)

@app.route('/')
def home():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        return "Hello Boss!  <a href='/logout'>Logout</a>"

@app.route('/login', methods=['POST'])
def do_admin_login():
    return "This is a login Page"

@app.route("/printlabels")
def print_label():
    return render_template('printlabels.html')

@app.route("/logout")
def logout():
    session['logged_in'] = False
    return home()

@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404

if __name__ == "__main__":
    # app.run(host='0.0.0.0', port=80)
    app.secret_key = os.urandom(12)
    app.run(debug=True,host='0.0.0.0', port=4000)

