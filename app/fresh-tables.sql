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
    Name TEXT,
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
    RequestedForOrder INTEGER,
    AllocatedToOrder INTEGER,
    FOREIGN KEY(OrderID) REFERENCES Orders(OrderID) ON UPDATE CASCADE ON DELETE CASCADE,
    FOREIGN KEY(ProductID) REFERENCES Products(ProductID) ON UPDATE CASCADE ON DELETE CASCADE
);
-- Hydrate with dummy data
INSERT INTO Ingredients (
        Name,
        Description,
        MinimumOrderQuantity,
        QuantityStocked,
        QuantityAllocated,
        QuantityConsumed
    )
VALUES ('Gummy Base', '', 1000, 8000, 8000, 3000),
    ('Vitamin C', '', 25, 100, 80, 120),
    ('Melatonin', '', 10, 20, 0, 0),
    ('Vitamin A', '', 15, 50, 80, 0),
    ('Vitamin B', '', 15, 50, 80, 0);
INSERT INTO Products (
        Name,
        Description,
        MinimumBatchSize,
        UnitsStocked,
        UnitsAllocated,
        UnitsFulfilled
    )
VALUES (
        'ImmuneBoost',
        'just vitamin c + gummy',
        100,
        300,
        200,
        300
    ),
    ('SleepRite', 'melatonin + gummy', 100, 0, 0, 0),
    (
        'Alphabetter',
        'vitamins abc + gummy',
        200,
        100,
        0,
        0
    );
INSERT INTO Orders (OrderID, Status, Name)
VALUES (1, 'Open', 'CVS Restock'),
    (2, 'Open', 'Target Batch'),
    (3, 'Procurement', 'Amazon Fulfillment'),
    (4, 'Production', 'Southeastern Grocers'),
    (5, 'Fulfilled', 'Farmer John');
/*
 1. 2 ImmuneBoost and 1 Alphabetter - OPEN
 2. 10 SleepRite - OPEN
 3. 5 Alphabetter - Procurement
 4. 4 Alphabetter - Production
 5. 3 ImmuneBoost - Fulfilled
 */
INSERT INTO OrderProducts (
        OrderID,
        ProductID,
        RequestedForOrder,
        AllocatedToOrder
    )
VALUES (
        1,
        (
            SELECT ProductID
            FROM Products p
            WHERE p.Name == 'ImmuneBoost'
        ),
        2000,
        0
    ),
    (
        1,
        (
            SELECT ProductID
            FROM Products p
            WHERE p.Name == 'Alphabetter'
        ),
        1000,
        0
    ),
    (
        2,
        (
            SELECT ProductID
            FROM Products p
            WHERE p.Name == 'SleepRite'
        ),
        10 * 100,
        0
    ),
    (
        3,
        (
            SELECT ProductID
            FROM Products p
            WHERE p.Name == 'Alphabetter'
        ),
        5 * 1000,
        0
    ),
    (
        4,
        (
            SELECT ProductID
            FROM Products p
            WHERE p.Name == 'Alphabetter'
        ),
        4 * 1000,
        0
    ),
    (
        5,
        (
            SELECT ProductID
            FROM Products p
            WHERE p.Name == 'ImmuneBoost'
        ),
        3 * 1000,
        3000
    );
/*
 1. ImmuneBoost - 100 UnitsProduced from 40 Vitamin C + 1000 Gummy Base
 2. SleepRite - 100 UnitsProduced from 20 Melatonin + 1000 Gummy Base
 3. Alphabetter - 200 UnitsProduced from 20 each of Vitamins A, B, and C + 2000 Gummy Base
 */
INSERT INTO ProductIngredients (
        ProductID,
        IngredientID,
        IngredientQuantity
    )
VALUES (
        (
            SELECT ProductID
            FROM Products p
            WHERE p.Name == 'ImmuneBoost'
        ),
        (
            SELECT IngredientID
            FROM Ingredients i
            WHERE i.Name == 'Vitamin C'
        ),
        40
    ),
    (
        (
            SELECT ProductID
            FROM Products p
            WHERE p.Name == 'ImmuneBoost'
        ),
        (
            SELECT IngredientID
            FROM Ingredients i
            WHERE i.Name == 'Gummy Base'
        ),
        1000
    ),
    (
        (
            SELECT ProductID
            FROM Products p
            WHERE p.Name == 'SleepRite'
        ),
        (
            SELECT IngredientID
            FROM Ingredients i
            WHERE i.Name == 'Gummy Base'
        ),
        1000
    ),
    (
        (
            SELECT ProductID
            FROM Products p
            WHERE p.Name == 'SleepRite'
        ),
        (
            SELECT IngredientID
            FROM Ingredients i
            WHERE i.Name == 'Melatonin'
        ),
        20
    ),
    (
        (
            SELECT ProductID
            FROM Products p
            WHERE p.Name == 'Alphabetter'
        ),
        (
            SELECT IngredientID
            FROM Ingredients i
            WHERE i.Name == 'Gummy Base'
        ),
        2000
    ),
    (
        (
            SELECT ProductID
            FROM Products p
            WHERE p.Name == 'Alphabetter'
        ),
        (
            SELECT IngredientID
            FROM Ingredients i
            WHERE i.Name == 'Vitamin A'
        ),
        20
    ),
    (
        (
            SELECT ProductID
            FROM Products p
            WHERE p.Name == 'Alphabetter'
        ),
        (
            SELECT IngredientID
            FROM Ingredients i
            WHERE i.Name == 'Vitamin B'
        ),
        20
    ),
    (
        (
            SELECT ProductID
            FROM Products p
            WHERE p.Name == 'Alphabetter'
        ),
        (
            SELECT IngredientID
            FROM Ingredients i
            WHERE i.Name == 'Vitamin C'
        ),
        20
    );