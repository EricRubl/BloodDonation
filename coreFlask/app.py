from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/core')
def core():
    return 'in core'


if __name__ == '__main__':
    app.run(threaded=True)
