from flask import Blueprint, render_template, request
from . import database as db
from . import orders


bp = Blueprint("main", __name__)


@bp.route("/")
@bp.route("/dashboard")
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


@bp.route("/orders")
def get_orders():
    cxn = db.get_db()
    all_orders = orders.get_all_orders(cxn)
    return render_template("orders-manage.html", orders=all_orders)


@bp.route("/orders/<int:order_id>", methods=["GET", "PUT"])
def get_order_details(order_id):
    cxn = db.get_db()
    order_details = orders.get_order(cxn, order_id)
    products = orders.get_products(cxn, order_id)

    if request.method == "PUT":
        updated_order = {
            "name": request.form.get("order-name"),
            "status": request.form.get("order-status"),
        }
        updated_products = extract_product_updates()

        affected_order = orders.update_order(cxn, order_id, updated_order)
        affected_products = orders.update_products(cxn, order_id, updated_products)
        order_details = orders.get_order(cxn, order_id)
        products = orders.get_products(cxn, order_id)

    if request.headers.get("HX-Request"):
        return render_template(
            "order-detail.html", order=order_details, products=products
        )
    return render_template(
        "order-detail-page.html", order=order_details, products=products
    )


def extract_product_updates() -> dict[int, dict[str, int]]:
    """used to process request updating product assignments on an order"""
    updated_products = {}
    for k, v in request.form.items():
        if k.startswith("product-requested"):
            op_id = int(k.split("-")[-1])
            updated_products[op_id] = updated_products.get(op_id, {}) | {
                "requested": int(v)
            }
        if k.startswith("product-allocated"):
            op_id = int(k.split("-")[-1])
            updated_products[op_id] = updated_products.get(op_id, {}) | {
                "allocated": int(v)
            }
    return updated_products


@bp.route("/orders/<int:order_id>/edit")
def order_edit_form(order_id, methods=["GET", "PUT"]):

    cxn = db.get_db()
    order_details = orders.get_order(cxn, order_id)
    products = orders.get_products(cxn, order_id)

    if request.headers.get("HX-Request"):
        return render_template(
            "order-edit.html", order=order_details, products=products
        )
    return render_template(
        "order-edit-page.html", order=order_details, products=products
    )


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
