import sys
from sys import stderr
import pprint
from flask import Flask, render_template, request, jsonify
from flask_cors import cross_origin, CORS
from flask_login import LoginManager, UserMixin, login_user, logout_user, current_user, login_required
from models_user import *
from init import *

login_manager = LoginManager(app)
login_manager.login_view = 'login'

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def my_index():
    return render_template("index.html", token=" Chris Pantani")


@app.route('/login_user', methods=['POST'])
@cross_origin()
def login_user():
    content = request.json
    pprint.pprint(content)
    q = db.session.query(User).filter(User.email == content["email"]).first()
    if q:
        data = {
            "logged_in": True,
            "user": {
                "email": q.get_email(),
                "id": q.get_id(),
                "password": ""

            }
        }
    else:
        data = {
            "logged_in": False,
            "user": {}
        }
    return data


@app.route('/signup_user', methods=['POST'])
@cross_origin()
def signup_user():
    content = request.json
    pprint.pprint(content)
    q = db.session.query(User).filter(User.email == content["email"]).first()

    if q is None:
        s = User(firstName=content["firstName"],lastName=content["lastName"], email=content["email"], password=content["password"], role="user")
        db.session.add(s)
        db.session.commit()

        x = db.session.query(User).filter(User.email == content["email"]).first()

        data = {
            "logged_in": True,
            "user": {
                "email": x.get_email(),
                "id": x.get_id(),
                "password": ""
            }
        }
    return data


class LoginUser(UserMixin):
    def __init__(self, username, password, role):
        self.ID = username
        self.password = password
        self.role = role


def getUser():
    return current_user.ID

@login_manager.user_loader
def load_user(username):
    login_obj = User.querry.filter_by(username=username).first()
    return LoginUser(login_obj.username, login_obj.password, login_obj.role)


if __name__ == '__main__':
    app.run()
