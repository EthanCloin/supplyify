from flask import Flask, render_template, request


app = Flask(__name__)
app.secret_key = b"think of the children"


@app.route("/")
def home():
    return render_template("dashboard.html", request={"request": request})


if __name__ == "__main__":
    app.run(debug=True)
