from flask import Blueprint, render_template, request
from . import database as db
from . import orders


bp = Blueprint("main", __name__)


@bp.route("/")
def home():
    dashboard = get_dashboard_data()
    return render_template("dashboard.html", **dashboard)


@bp.route("/products")
def get_products():
    order_id = request.args.get("orderId")
    if order_id is not None:
        order_id = int(order_id)
        products = get_products_on_order(order_id)
        return render_template("order-products-table.html", products=products)
    return "<tbody></tbody>"


def get_dashboard_data():
    cxn = db.get_db()
    all_orders = orders.get_all_orders(cxn)
    order_status_counts = orders.get_order_counts_by_status(cxn)
    return {
        "orders": all_orders,
        "counts": order_status_counts,
    }


def get_products_on_order(order_id: int):
    cxn = db.get_db()
    products = orders.get_products(cxn, order_id)
    return products
