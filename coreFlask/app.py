from flask import Flask, request

from Dispatcher.Controller import Controller

app = Flask(__name__)
ctrl = Controller()


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/core/get/donors', methods=['GET'])
def core_get_donors():
    return_data = ctrl.get_all_donors()
    print(return_data)
    return str(return_data)


@app.route('/core/get/doctors', methods=['GET'])
def core_get_doctors():
    return_data = ctrl.get_all_doctors()
    print(return_data)
    return str(return_data)


@app.route('/core/get/donations', methods=['GET'])
def core_get_donations():
    return_data = ctrl.get_all_donations()
    print(return_data)
    return str(return_data)


@app.route('/core/get/hospitals', methods=['GET'])
def core_get_hospitals():
    return_data = ctrl.get_all_hospitals()
    print(return_data)
    return str(return_data)


@app.route('/core/get/requests', methods=['GET'])
def core_get_requests():
    return_data = ctrl.get_all_requests()
    print(return_data)
    return str(return_data)


@app.route('/core/get/status-updates', methods=['GET'])
def core_get_status_update():
    return_data = ctrl.get_all_status_updates()
    print(return_data)
    return str(return_data)


if __name__ == '__main__':
    app.run(threaded=True)
