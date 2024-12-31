from flask import Flask, request, render_template

app = Flask(__name__)


@app.route("/form", methods=["GET", "POST"])
def form():
    if request.method == "POST":
        name = request.form["name"]  # Correct way to access form data
        email = request.form["email"]
        return f"Hello {name}! Your email is {email}"
    return render_template("form.html")


@app.route("/submit", methods=["GET", "POST"])
def submit():
    if request.method == "POST":
        name = request.form["name"]  # Correct way to access form data
        email = request.form["email"]
        return f"Hello {name}! Your email is {email}"
    return render_template("form.html")


if __name__ == "__main__":
    app.run(debug=True)
