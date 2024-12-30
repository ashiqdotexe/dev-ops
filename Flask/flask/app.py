from flask import Flask

"""
It works as a webserver gateway interface application
"""
app = Flask(__name__)  ###Wsgi Application


@app.route("/")
def welcome():
    return "Welcome to this Flask course"


@app.route("/index")
def index():
    return "Welcome to index"


if __name__ == "__main__":
    app.run(debug=True)
