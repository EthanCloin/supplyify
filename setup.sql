-- build all the tables, dropping first to start fresh
DROP TABLE IF EXISTS Ingredients;
CREATE TABLE Ingredients (
    IngredientID INTEGER PRIMARY KEY,
    Name TEXT,
    Description TEXT,
    MinimumOrderQuantity INTEGER,
    QuantityStocked INTEGER,
    QuantityAllocated INTEGER,
    QuantityConsumed INTEGER
);
DROP TABLE IF EXISTS Products;
CREATE TABLE Products (
    ProductID INTEGER PRIMARY KEY,
    Name TEXT,
    Description TEXT,
    MinimumBatchSize INTEGER,
    UnitsStocked INTEGER,
    UnitsAllocated INTEGER,
    UnitsFulfilled INTEGER
);
DROP TABLE IF EXISTS Orders;
CREATE TABLE Orders (
    OrderID INTEGER PRIMARY KEY,
    Status TEXT CHECK(
        Status IN ('Open', 'Procurement', 'Production', 'Fulfilled')
    )
);
DROP TABLE IF EXISTS ProductIngredients;
CREATE TABLE ProductIngredients (
    ProductIngredientsID INTEGER PRIMARY KEY,
    ProductID INTEGER,
    IngredientID INTEGER,
    IngredientQuantity INTEGER,
    FOREIGN KEY(ProductID) REFERENCES Products(ProductID) ON UPDATE CASCADE ON DELETE CASCADE,
    FOREIGN KEY(IngredientID) REFERENCES Ingredients(IngredientID) ON UPDATE CASCADE ON DELETE CASCADE
);
DROP TABLE IF EXISTS OrderProducts;
CREATE TABLE OrderProducts (
    OrderProductsID INTEGER PRIMARY KEY,
    OrderID INTEGER,
    ProductID INTEGER,
    UnitsRequested INTEGER,
    FOREIGN KEY(OrderID) REFERENCES Orders(OrderID) ON UPDATE CASCADE ON DELETE CASCADE,
    FOREIGN KEY(ProductID) REFERENCES Products(ProductID) ON UPDATE CASCADE ON DELETE CASCADE
);