from flask import Flask

app = Flask(__name__)

if __name__ == '__main_':
    app.run(
        host='0.0.0.0.',
        port=7000,
        debug=True
    )