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


def get_products(db: Connection, order_id: int):
    query = """
SELECT 
    p.Name
    ,op.RequestedForOrder as Requested
    ,op.AllocatedToOrder as Allocated
    ,p.UnitsStocked as Available
    ,(op.RequestedForOrder - op.AllocatedToOrder) As Unfulfilled
FROM Products p
JOIN OrderProducts op ON op.ProductID = p.ProductID
WHERE op.OrderID = ?
ORDER BY p.Name ASC;
"""
    rows = db.execute(query, (order_id,)).fetchall()
    return rows
