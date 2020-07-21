from flask import Flask, render_template, request, jsonify
from flask_cors import cross_origin, CORS
from flask_login import LoginManager, UserMixin, login_user, logout_user, current_user, login_required
from models_user import *
from init import *

login_manager = LoginManager(app)
login_manager.login_view = 'login'

app = Flask(__name__)


class LoginUser(UserMixin):
    def __init__(self, username, password, role):
        self.ID = username
        self.password = password
        self.role = role


def getUser():
    return current_user.ID


def adduser():
    login_obj = User.querry.filter_by(username=  ).first()
    if login_obj = None:
        u=User(  )
        db.session.add(u)
        db.session.commit()


@login_manager.user_loader
def load_user(username):
    login_obj = User.querry.filter_by(username=username).first()
    return LoginUser(login_obj.username, login_obj.password, login_obj.role)


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template("index.html", token="Add user")


@app.route('/api_post', methods=['POST'])
@cross_origin()
def my_api_post():
    content = request.json

    return jsonify()


if __name__ == '__main__':
    app.run()
