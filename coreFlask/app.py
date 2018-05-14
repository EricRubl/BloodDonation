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
        self.id = _id
        self.type = None

    # def __repr__(self):
    #     return "%s/%s" % (self.name, self.password)


# create some users with ids 1 to 20
# users = User("asd")


@app.route('/doc')
def doc():
    return app.send_static_file("doctor.html")


@app.route('/')
def index():
    if current_user.is_authenticated:
        print(current_user)
        return Response("Asa mai merge wee")
    return redirect('/login')


# somewhere to login
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user_type = ctrl.get_user_type(username, password)
        if user_type is None:
            return abort(401)
        elif user_type == 'Donor':
            _id = username
            user = User(_id)
            user.type = 'Donor'
            login_user(user)
            return redirect('/donor')
        elif user_type == 'Doctor':
            _id = username
            user = User(_id)
            user.type = 'Doctor'
            login_user(user)
            return redirect('/doctor')
        elif user_type == 'Personnel':
            _id = username
            user = User(_id)
            user.type = 'Personnel'
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


# somewhere to logout
@app.route("/logout")
# @login_required
def logout():
    if current_user.is_authenticated:
        logout_user()
        return Response('<p>Logged out</p>')
    return redirect('/')


# somewhere to logout
@app.route("/doctor")
# @login_required
def doctor_dashboard():
    if current_user.is_authenticated and current_user.type == 'Doctor':
        return "ai ajuns unde trebe"
    return "ai supto"


# handle login failed
@app.errorhandler(401)
def page_not_found(e):
    return Response('<p>Login failed</p> ' + str(e))


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


@app.route('/autori')
def autori():
    return 'pogra & erwick'


if __name__ == '__main__':
    app.run(threaded=True)
