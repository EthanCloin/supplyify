from sqlite3 import Connection


def get_all_orders(db: Connection):
    query = """SELECT
    OrderID 
    ,Name
    ,Status
FROM Orders
"""

    res = db.execute(query).fetchall()
    return res


def get_order_counts_by_status(db: Connection):
    query = """SELECT 
    Status
    ,COUNT(*) AS Count
FROM Orders
WHERE Status IN ('Open', 'Procurement', 'Production')
GROUP BY Status"""
    rows = db.execute(query).fetchall()
    counts = {
        "open": rows[0]["count"],
        "procurement": rows[1]["count"],
        "production": rows[2]["count"],
    }
    return counts


def get_order(db: Connection, order_id: int):

    query = """SELECT
    OrderID 
    ,Name
    ,Status
FROM Orders
WHERE OrderID = ?;
"""
    order = db.execute(query, (order_id,)).fetchone()
    return order


def get_products(db: Connection, order_id: int):
    query = """
SELECT 
    p.Name
    ,op.RequestedForOrder as Requested
    ,op.AllocatedToOrder as Allocated
    ,p.UnitsStocked as Available
    ,(op.RequestedForOrder - op.AllocatedToOrder) As Unfulfilled
    ,op.OrderProductsID
FROM Products p
JOIN OrderProducts op ON op.ProductID = p.ProductID
WHERE op.OrderID = ?
ORDER BY p.Name ASC;
"""
    rows = db.execute(query, (order_id,)).fetchall()
    return rows


def update_order(db: Connection, order_id: int, order: dict):
    query = """
UPDATE Orders
SET 
    Name = ?
    ,Status = ?
WHERE OrderID = ?
RETURNING OrderID;
"""
    #
    affected_order = db.execute(
        query, (order.get("name"), order.get("status"), order_id)
    ).fetchone()
    db.commit()
    return affected_order


def update_products(
    db: Connection, order_id: int, order_products: dict[int, dict[str, int]]
):
    query = """
UPDATE OrderProducts
SET
    RequestedForOrder = ?
    ,AllocatedToOrder = ?
WHERE
    OrderProductsID = ?
RETURNING OrderProductsID
    """
    affected_products = []
    for op_id, vals in order_products.items():
        params = (vals.get("requested"), vals.get("allocated"), op_id)
        affected_products.append(db.execute(query, params).fetchone())
    db.commit()
    return affected_products
