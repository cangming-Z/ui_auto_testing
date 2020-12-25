from flask import render_template, redirect, url_for, Blueprint, request, jsonify
from flask_login import current_user, login_user, login_required, logout_user

auth_bp = Blueprint('auth', __name__)


@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('todo.app'))

    if request.method == 'POST':
        data = request.get_json()
        username = data['username']
        password = data['password']

        if username == 'abc' and password == '123':
            login_user(username)
            return jsonify(message=_('Login success.'))
        return jsonify(message=_('Invalid username or password.')), 400
    return render_template('_login.html')


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