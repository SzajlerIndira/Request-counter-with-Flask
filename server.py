from flask import Flask, render_template, redirect, request, session

app = Flask(__name__)

counts = 0

@app.route('/request-counter')
def counting():
    counts += 1
    return render_template('index.html')
if __name__ == '__main_':
    app.run(
        host='0.0.0.0.',
        port=7000,
        debug=True
    )