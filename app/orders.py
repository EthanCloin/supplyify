from sqlite3 import Connection


def get_all_orders(db: Connection):
    query = """
SELECT (
    OrderID
    ,Name
)
FROM Orders
    """

    res = db.execute(query).fetchall()
    return res


# def get_order_dashboard
