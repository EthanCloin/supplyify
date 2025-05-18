from flask import Blueprint, render_template, request
from . import database as db
from . import orders


bp = Blueprint("main", __name__)


@bp.route("/")
def home():
    dashboard = get_dashboard_data()

    return render_template("dashboard.html", **dashboard)


def get_dashboard_data():
    cxn = db.get_db()
    all_orders = orders.get_all_orders(cxn)
    order_status_counts = orders.get_order_counts_by_status(cxn)
    return {
        "orders": all_orders,
        "counts": order_status_counts,
    }
