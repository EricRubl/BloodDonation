from flask import Response, request, redirect, abort
from flask_login import current_user, login_user, logout_user

from API import ctrl, User


def login_user_endpoint():
    if current_user.is_authenticated:
        return redirect('/')
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user_type = ctrl.get_user_type(username, password)
        if user_type is None:
            return abort(401)
        elif user_type == 'Donor':
            _id = username
            user = User(_id)
            # user.type = 'Donor'
            login_user(user)
            return redirect('/donor')
        elif user_type == 'Doctor':
            _id = username
            user = User(_id)
            # user.type = 'Doctor'
            login_user(user)
            return redirect('/doctor')
        elif user_type == 'Personnel':
            _id = username
            user = User(_id)
            # user.type = 'Personnel'
            login_user(user)
            return redirect('/personnel')
        else:
            return abort(401)
    else:
        return Response('''
        <form action="" method="post">
            <p><input type=text name=username>
            <p><input type=password name=password>
            <p><input type=submit value=Login>
        </form>
        ''')


def logout_user_endpoint():
    if current_user.is_authenticated:
        logout_user()
        return Response('<p>Logged out</p>')
    return redirect('/')
