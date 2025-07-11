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
    counts = {"open": 0, "procurement": 0, "production": 0}
    for r in rows:
        counts[r["status"].lower()] = r["count"]

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


def create_order(db: Connection, order: dict, order_products: list[dict]):
    order_query = """
INSERT INTO Orders (Name, Status) VALUES (?, ?);
"""
    order_params = (order.get("Name"), order.get("Status"))
    cursor = db.execute(order_query, order_params)
    order_id = cursor.lastrowid

    op_query = """
INSERT INTO OrderProducts (OrderID, ProductID, RequestedForOrder) VALUES (?, ?, ?);
"""
    
    op_params = [(order_id, op.get("ProductID"), op.get("RequestedForOrder")) for op in order_products]
    db.executemany(op_query, op_params)
    db.commit()
    # Example with sqlite3
    


    
