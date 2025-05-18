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
    res = db.execute(query).fetchall()
    better = {
        "open": res[0]["count"],
        "procurement": res[1]["count"],
        "production": res[2]["count"],
    }
    return better
