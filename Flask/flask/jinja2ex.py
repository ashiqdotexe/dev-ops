from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)


@app.route("/result/<int:score>")
def result(score):
    res = ""
    if score > 50:
        res = "Passed"
    else:
        res = "Failed"
    return render_template("finalresult.html", results=res)


@app.route("/resultfor/<int:score>")
def resultfor(score):
    res = ""
    if score > 50:
        res = "Passed"
    else:
        res = "Failed"
    exp = {"score": score, "result": res}
    return render_template("result.html", results=exp)


@app.route("/submit", methods=["POST", "GET"])
def submit():
    total_score = 0
    if request.method == "POST":
        science = float(request.form["science"])
        maths = float(request.form["maths"])
        c = float(request.form["c"])
        data_science = float(request.form["datascience"])
        total_score = (science + maths + c + data_science) / 4
    else:
        return render_template("submit.html")
    return redirect(url_for("resultfor", score=total_score))


if __name__ == "__main__":
    app.run(debug=True)
