from sqlite3 import Connection


def get_all_products(db: Connection):
    query = """
SELECT 
    ProductID 
    ,Name
    ,MinimumBatchSize
FROM Products;
"""
    res = db.execute(query).fetchall()
    return [dict(p) for p in res]
