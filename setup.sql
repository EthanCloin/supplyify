CREATE TABLE Ingredients (
    IngredientID INTEGER PRIMARY KEY,
    Name TEXT,
    Description TEXT,
    MinimumOrderQuantity INTEGER,
    QuantityStocked INTEGER,
    QuantityAvailable INTEGER
);

CREATE TABLE Products (
    ProductID INTEGER PRIMARY KEY,
    Name TEXT,
    Description TEXT,
    UnitsStocked INTEGER,
    UnitsAvailable INTEGER
);

CREATE TABLE Orders (
    OrderID INTEGER PRIMARY KEY,
    Status TEXT CHECK(Status IN ('Open', 'In Procurement', 'In Production', 'Fulfilled'))
);

CREATE TABLE ProductIngredients (
    ProductIngredientsID INTEGER PRIMARY KEY,
    ProductID INTEGER,
    IngredientID INTEGER,
    QuantityRequired INTEGER,
    UnitsProduced INTEGER,
    FOREIGN KEY(ProductID) REFERENCES Products(ProductID)
    FOREIGN KEY(IngredientID) REFERENCES Ingredients(IngredientID)
);

CREATE TABLE OrderProducts (
    OrderProductsID INTEGER PRIMARY KEY,
    OrderID INTEGER,
    ProductID INTEGER,
    UnitsRequested INTEGER,
    FOREIGN KEY(OrderID) REFERENCES Orders(OrderID),
    FOREIGN KEY(ProductID) REFERENCES Products(ProductID)
);