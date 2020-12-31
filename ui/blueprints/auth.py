import json

from flask import render_template, redirect, url_for, Blueprint, request, jsonify
from flask_login import current_user, login_user, login_required, logout_user

auth_bp = Blueprint('auth', __name__)


@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        try:
            data = request.get_data()
            json_data = json.loads(data)
            username = json_data['username']
            password = json_data['password']

            if username == '' and password == '':
                # login_user(username)
                return 'main'
            return jsonify(message='Invalid username or password.'), 400
        except Exception as e:
            print(e)
            return jsonify(message='error')


@auth_bp.route('/logout')
@login_required
def logout():
    logout_user()
    return jsonify(message=_('Logout success.'))


@auth_bp.route('/register')
def register():
    username = 'aaa'
    password = '123'
    # generate a random account for demo use
    # username = fake.user_name()
    # # make sure the generated username was not in database
    # while User.query.filter_by(username=username).first() is not None:
    #     username = fake.user_name()
    # password = fake.word()
    # user = User(username=username)
    # user.set_password(password)
    # db.session.add(user)
    # db.session.commit()
    return jsonify(username=username, password=password, message=_('Generate success.'))