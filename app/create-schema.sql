
-- build all the tables, dropping first to start fresh
CREATE TABLE IF NOT EXISTS Ingredients (
    IngredientID INTEGER PRIMARY KEY,
    Name TEXT,
    Description TEXT,
    MinimumOrderQuantity INTEGER,
    QuantityStocked INTEGER,
    QuantityAllocated INTEGER,
    QuantityConsumed INTEGER
);
CREATE TABLE IF NOT EXISTS Products (
    ProductID INTEGER PRIMARY KEY,
    Name TEXT,
    Description TEXT,
    MinimumBatchSize INTEGER,
    UnitsStocked INTEGER,
    UnitsAllocated INTEGER,
    UnitsFulfilled INTEGER
);

CREATE TABLE IF NOT EXISTS Orders (
    OrderID INTEGER PRIMARY KEY,
    Status TEXT CHECK(
        Status IN ('Open', 'Procurement', 'Production', 'Fulfilled')
    )
);
CREATE TABLE IF NOT EXISTS ProductIngredients (
    ProductIngredientsID INTEGER PRIMARY KEY,
    ProductID INTEGER,
    IngredientID INTEGER,
    IngredientQuantity INTEGER,
    FOREIGN KEY(ProductID) REFERENCES Products(ProductID) ON UPDATE CASCADE ON DELETE CASCADE,
    FOREIGN KEY(IngredientID) REFERENCES Ingredients(IngredientID) ON UPDATE CASCADE ON DELETE CASCADE
);
CREATE TABLE IF NOT EXISTS OrderProducts (
    OrderProductsID INTEGER PRIMARY KEY,
    OrderID INTEGER,
    ProductID INTEGER,
    UnitsRequested INTEGER,
    FOREIGN KEY(OrderID) REFERENCES Orders(OrderID) ON UPDATE CASCADE ON DELETE CASCADE,
    FOREIGN KEY(ProductID) REFERENCES Products(ProductID) ON UPDATE CASCADE ON DELETE CASCADE
);
