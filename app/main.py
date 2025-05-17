from flask import Blueprint, render_template, request


bp = Blueprint("main", __name__)
bp.secret_key = b"think of the children"


@bp.route("/")
def home():
    return render_template("dashboard.html", request={"request": request})


if __name__ == "__main__":
    bp.run(debug=True)
