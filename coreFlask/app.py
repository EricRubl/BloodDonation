from flask import Flask, Response, redirect, request, abort
from flask_login import LoginManager, UserMixin, login_required, current_user

from API import AccountAPI
from API import ctrl

app = Flask(__name__)
app.config.update(
    DEBUG=True,
    SECRET_KEY="super_secret"
)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"


class User(UserMixin):
    def __init__(self, name):
        self.id = name
        self.password = ctrl.get_user_password(self.id)
        self.type = ctrl.get_user_type(self.id, self.password)


@app.route('/')
def index():
    if current_user.is_authenticated:
        return Response("Asa mai merge wee %s cu parola %s fiind un %s" %
                        (current_user.id, current_user.password, current_user.type))
    return redirect('/login')


# somewhere to login
@app.route("/login", methods=["GET", "POST"])
def login():
    return AccountAPI.login_user_endpoint()


# somewhere to logout
@app.route("/logout")
def logout():
    return AccountAPI.logout_user_endpoint()


@app.route('/user')
@login_required
def get_current_user():
    return str(current_user.id)


@app.errorhandler(401)
def page_not_found(e):
    return Response('<p>Login failed</p> ' + str(e))


# handle login failed
@login_manager.user_loader
def load_user(user_id):
    return User(user_id)


@app.route("/doctor")
@login_required
def doctor_dashboard():
    if current_user.is_authenticated and current_user.type == 'Doctor':
        return app.send_static_file("doctor.html")
    return app.send_static_file("doctor.html")


@app.route("/donor")
@login_required
def donor_dashboard():
    if current_user.is_authenticated and current_user.type == 'Donor':
        return app.send_static_file("donor.html")
    return app.send_static_file("donor.html")


@app.route("/personnel")
@login_required
def personnel_dashboard():
    if current_user.is_authenticated and current_user.type == 'Personnel':
        return app.send_static_file("personnel.html")
    return app.send_static_file("personnel.html")


@app.route('/core/get/donors', methods=['GET'])
@login_required
def core_get_donors():
    return str(ctrl.get_all_donors())


@app.route('/core/get/donorbyname', methods=['GET', 'POST'])
@login_required
def core_get_donor_by_name():
    if not request.args:
        return abort(400)
    return str(ctrl.get_donor_by_name(request.args['name']))


@app.route('/core/get/donationsbydonor', methods=['GET', 'POST'])
@login_required
def core_get_donations_by_donor():
    if not request.args:
        return abort(400)
    return str(ctrl.get_donations_by_donor(request.args['name']))


@app.route('/core/get/labresultbydonation', methods=['GET', 'POST'])
@login_required
def core_get_lab_result_by_donation():
    if not request.args:
        return abort(400)
    return str(ctrl.get_lab_results_by_donation(request.args['donation']))


@app.route('/core/get/doctorbyname', methods=['GET', 'POST'])
@login_required
def core_get_doctor_by_name():
    if not request.args:
        return abort(400)
    return str(ctrl.get_doctor_by_name(request.args['name']))


@app.route('/core/get/requestsbydoctor', methods=['GET', 'POST'])
@login_required
def core_get_requests_by_doctor():
    if not request.args:
        return abort(400)
    return str(ctrl.get_requests_by_doctor(request.args['name']))


@app.route('/core/get/statusupdatebyrequest', methods=['GET', 'POST'])
@login_required
def core_get_status_update_by_request():
    if not request.args:
        return abort(400)
    return str(ctrl.get_status_updates_by_request(request.args['request']))


@app.route('/core/post/updaterequestpriority', methods=['GET', 'POST'])
@login_required
def core_post_update_request_priority():
    if not request.args:
        return abort(400)
    return str(ctrl.update_request_priority(request.args['request'], request.args['priority']))


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
