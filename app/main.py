from flask import Blueprint, render_template, request, redirect, url_for
from . import database as db
from . import orders, products


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
    if request.headers.get("HX-Request"):
        return render_template("orders-manage.html", orders=all_orders)
    return render_template("orders-manage-page.html", orders=all_orders)


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


@bp.route("/orders/<int:order_id>/edit", methods=["GET", "PUT"])
def order_edit_form(order_id):

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


@bp.get("/orders/new")
def order_new_form():
    cxn = db.get_db()
    all_products = products.get_all_products(cxn)
    return render_template("order-create.html", products=all_products)


@bp.post("/orders/new")
def create_new_order():
    # Build a list of dicts with ProductID, Name, Quantity
    products_requested = []
    for key, value in request.form.items():
        if key.startswith("product-name-"):
            idx = key.split("-")[-1]
            product_id = value
            quantity_key = f"product-requested-{idx}"
            quantity = request.form.get(quantity_key)
            if product_id and quantity:
                try:
                    quantity_int = int(quantity)
                except ValueError:
                    continue
                products_requested.append({
                    "ProductID": int(product_id),
                    "RequestedForOrder": quantity_int
                })
    order = {
        "Name": request.form.get("order-name"),
        "Status": request.form.get("order-status"),
    }
    cxn = db.get_db()
    orders.create_order(cxn, order, products_requested)
    return redirect(url_for("main.get_orders"))

@bp.get("/products/new")
def product_new_form():
    return render_template("product-create.html")

@bp.post("/products/new")
def create_new_product():
    product = {
        "Name": request.form.get("product-name"),
        "Description": request.form.get("product-description"),
        "MinimumBatchSize": int(request.form.get("product-min-batch")),
        "UnitsStocked": int(request.form.get("product-units-stocked")),
    }
    cxn = db.get_db()
    products.create_product(cxn, product)
    return redirect(url_for("main.get_orders"))

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
