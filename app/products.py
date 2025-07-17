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

def create_product(db: Connection, product: dict):
    query = """
INSERT INTO Products (Name, Description, MinimumBatchSize, UnitsStocked) VALUES (?, ?, ?, ?);
"""
    params = (product.get("Name"), product.get("Description"), product.get("MinimumBatchSize"), product.get("UnitsStocked"))
    cursor = db.execute(query, params)
    db.commit()
    return cursor.lastrowid