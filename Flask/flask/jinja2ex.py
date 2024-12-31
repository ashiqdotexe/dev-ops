from flask import Flask, request, render_template

app = Flask(__name__)


@app.route("/result/<int:score>")
def result(score):
    res = ""
    if score > 50:
        res = "Passed"
    else:
        res = "Failed"
    return render_template("result.html", results=res)


if __name__ == "__main__":
    app.run(debug=True)
