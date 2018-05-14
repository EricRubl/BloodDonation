from flask import Flask, Response, request, redirect, abort
from flask_login import LoginManager, UserMixin, login_required, login_user, logout_user, current_user

from Dispatcher.Controller import Controller

# from flask_login import LoginManager, UserMixin, login_required, login_user, logout_user

app = Flask(__name__)
app.config.update(
    DEBUG=True,
    SECRET_KEY="super_secret"
)
ctrl = Controller()

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"


# silly user model
class User(UserMixin):

    def __init__(self, _id):
        self.name = _id
        self.password = _id
        self.id = _id

    # def __repr__(self):
    #     return "%s/%s" % (self.name, self.password)


# create some users with ids 1 to 20
users = User("asd")


# some protected url
# @app.route('/')
# def home_2():
#     return Response("Nu ejti logat tata")


@app.route('/')
def home():
    if current_user.is_authenticated:
        return Response("Asa mai merge wee")
    return Response("nu esti logat")


# somewhere to login
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if password == "asd":
            _id = username.split('/')[0]
            user = User(_id)
            login_user(user)
            return redirect('/')
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


# somewhere to logout
@app.route("/logout")
# @login_required
def logout():
    if current_user.is_authenticated:
        logout_user()
        return Response('<p>Logged out</p>')
    return redirect('/')


# handle login failed
@app.errorhandler(401)
def page_not_found(e):
    return Response('<p>Login failed</p>')


# callback to reload the user object
@login_manager.user_loader
def load_user(user_id):
    print("In load user")
    return User(user_id)


#
# @app.route('/')
# def hello_world():
#     return 'Hello World!'
#
#
@app.route('/core/get/donors', methods=['GET'])
@login_required
def core_get_donors():
    return str(ctrl.get_all_donors())
#
#
# @app.route('/core/get/doctors', methods=['GET'])
# def core_get_doctors():
#     return str(ctrl.get_all_doctors())
#
#
# @app.route('/core/get/donations', methods=['GET'])
# def core_get_donations():
#     return str(ctrl.get_all_donations())
#
#
# @app.route('/core/get/hospitals', methods=['GET'])
# def core_get_hospitals():
#     return str(ctrl.get_all_hospitals())
#
#
# @app.route('/core/get/requests', methods=['GET'])
# def core_get_requests():
#     return str(ctrl.get_all_requests())
#
#
# @app.route('/core/get/status-updates', methods=['GET'])
# def core_get_status_update():
#     return str(ctrl.get_all_status_updates())


if __name__ == '__main__':
    app.run(threaded=True)
