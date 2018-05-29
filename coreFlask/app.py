import datetime

from flask import Flask, Response, redirect, request, abort
from flask_login import LoginManager, UserMixin, login_required, current_user, login_user, logout_user

from API import AccountAPI
from API import ctrl

app = Flask(__name__)
app.config.update(DEBUG=True, SECRET_KEY="super_secret")

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
        if current_user.type == 'Donor':
            return redirect('/donor')
        if current_user.type == 'Doctor':
            return redirect('/doctor')
        if current_user.type == 'Personnel':
            return redirect('/personnel')
    return redirect('/login')


# somewhere to login
@app.route("/login", methods=["GET", "POST"])
def login():
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
        return app.send_static_file("dashboard/login.html")


# somewhere to logout
@app.route("/logout")
def logout():
    if current_user.is_authenticated:
        logout_user()
    return redirect('/')


@app.route('/user', methods=['GET'])
@login_required
def get_current_user():
    return str(current_user.id)


@app.route('/forgot')
def forgot_password():
    return app.send_static_file('dashboard/forgot.html')


@app.route('/register')
def register_new_donor():
    return app.send_static_file('dashboard/register.html')


@app.errorhandler(401)
def page_not_found(e):
    return Response('<p>Login failed</p> ' + str(e))


@app.errorhandler(404)
def page_not_found_404(e):
    return app.send_static_file('404/index.html')


@app.errorhandler(500)
def http_500(e):
    return app.send_static_file('500/index.html')


# handle login failed
@login_manager.user_loader
def load_user(user_id):
    return User(user_id)


@app.route("/favicon.ico")
def get_favicon():
    return app.send_static_file("favicon.ico")


@app.route("/doctor")
@login_required
def doctor_dashboard():
    if current_user.is_authenticated and current_user.type == 'Doctor':
        return app.send_static_file("dashboard/doctor.html")
    return redirect('/')


@app.route("/donor")
@login_required
def donor_dashboard():
    if current_user.is_authenticated and current_user.type == 'Donor':
        return app.send_static_file("dashboard/donor.html")
    return redirect('/')


@app.route("/personnel")
@login_required
def personnel_dashboard():
    if current_user.is_authenticated and current_user.type == 'Personnel':
        return app.send_static_file("dashboard/personnel.html")
    return redirect('/')


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


@app.route('/core/post/insertrequest', methods=['GET', 'POST'])
@login_required
def core_post_insert_request():
    if not request.args:
        return abort(400)
    return str(ctrl.insert_new_request(current_user.id, request.args['priority'],
                                       request.args['blood'], request.args['quantity'],
                                       0, datetime.datetime.now()))


@app.route('/core/get/personnelbyname', methods=['GET', 'POST'])
@login_required
def core_get_personnel_by_name():
    if not request.args:
        return abort(400)
    return str(ctrl.get_personnel_by_name(request.args['name']))


@app.route('/core/get/requests', methods=['GET'])
@login_required
def core_get_requests():
    return str(ctrl.get_all_requests())


@app.route('/core/get/donations', methods=['GET'])
@login_required
def core_get_donations():
    return str(ctrl.get_all_donations())


@app.route('/core/get/donationsinbank', methods=['GET'])
@login_required
def core_get_donations_in_bank():
    return str(ctrl.get_donations_in_bank())


@app.route('/core/post/updaterequeststatus', methods=['GET', 'POST'])
@login_required
def core_update_request_status():
    if not request.args:
        return abort(400)
    return str(ctrl.update_request_status(request.args['id'], request.args['previous'], request.args['current'],
                                          request.args['personnel'], datetime.datetime.now()))


@app.route('/core/get/requestbyid', methods=['GET', 'POST'])
@login_required
def core_get_request_by_id():
    if not request.args:
        return abort(400)
    return str(ctrl.get_requests_by_id(request.args['id']))


@app.route('/core/post/insertlabresult', methods=['GET', 'POST'])
@login_required
def core_insert_lab_result():
    if not request.args:
        return abort(400)
    return str(ctrl.insert_lab_result(request.args['id'], request.args['syph'], request.args['hbv'],
                                      request.args['hiv'], request.args['hev'], request.args['htlv']))


@app.route('/core/post/movetobank', methods=['GET', 'POST'])
@login_required
def core_move_to_bank():
    if not request.args:
        return abort(400)
    return str(ctrl.move_donation_to_bank(request.args['id']))


@app.route('/core/post/assigntorequest', methods=['GET', 'POST'])
@login_required
def core_assign_to_request():
    if not request.args:
        return abort(400)
    return str(ctrl.assign_donation_to_request(request.args['req'], request.args['don']))


@app.route('/core/get/donationsofrequest', methods=['GET', 'POST'])
@login_required
def core_get_donations_of_request():
    if not request.args:
        return abort(400)
    return str(ctrl.get_donations_of_request(request.args['request']))


@app.route('/core/post/insertdonation', methods=['GET', 'POST'])
@login_required
def core_insert_donation():
    if not request.args:
        return abort(400)
    return str(ctrl.insert_donation(request.args['donor'], request.args['personnel'], datetime.datetime.now(),
                                    datetime.datetime.now() + datetime.timedelta(days=60), False))


@app.route('/core/get/donationswithoutlabs', methods=['GET'])
@login_required
def core_get_donations_without_labs():
    return str(ctrl.get_donations_without_labs())


@app.route('/core/get/readyforbank', methods=['GET'])
@login_required
def core_get_ready_for_bank():
    return str(ctrl.get_ready_for_bank())


@app.route('/core/get/readyforrequest', methods=['GET', 'POST'])
@login_required
def core_get_ready_for_request():
    if not request.args:
        return abort(400)
    return str(ctrl.get_ready_for_request(request.args['id']))


@app.route('/core/post/insertdonor', methods=['GET', 'POST'])
def core_insert_donor():
    if not request.args:
        return abort(400)
    a = request.args
    code = ctrl.insert_donor(a['name'], datetime.date(year=int(a['y']), month=int(a['m']), day=int(a['d'])), a['email'],
                             a['addr'], a['pass'],
                             a['blood'])
    if code == 'err':
        return code
    else:
        return redirect('/')


@app.route('/core/post/forgotpassword', methods=['GET', 'POST'])
def forgot_pass_request():
    if not request.args:
        return abort(400)
    args = request.args
    result = ctrl.forgot_password(args['email'], args['pass'])
    print(result)
    return 'err'


if __name__ == '__main__':
    app.run(threaded=True, host='0.0.0.0')
