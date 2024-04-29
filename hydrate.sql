-- Hydrate with dummy data
INSERT INTO Ingredients (
    Name,
    Description,
    MinimumOrderQuantity,
    QuantityStocked,
    QuantityAllocated,
    QuantityConsumed
) VALUES 
    ("Gummy Base", "", 1000, 8000, 8000, 3000),
    ("Vitamin C", "", 25, 100, 80, 120),
    ("Melatonin", "", 10, 20, 0, 0),
    ("Vitamin A", "", 15, 50, 80, 0),
    ("Vitamin B", "", 15, 50, 80, 0);

    INSERT INTO Products (
        Name,
        Description,
        ProducedPerOrder,
        UnitsStocked,
        UnitsAllocated,
        UnitsFulfilled
    ) VALUES
        ("ImmuneBoost", "just vitamin c + gummy", 100, 300, 200, 300),
        ("SleepRite", "melatonin + gummy", 100, 0, 0, 0),
        ("Alphabetter", "vitamins abc + gummy", 200, 100, 0, 0); 

INSERT INTO Orders (
    OrderID, Status
) VALUES
    (1, "Open"),
    (2, "Open"),
    (3, "Procurement"),
    (4, "Production"),
    (5, "Fulfilled");

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
    UnitsRequested
) VALUES
    (1, (SELECT ProductID FROM Products p WHERE p.Name == "ImmuneBoost"), 2000),
    (1, (SELECT ProductID FROM Products p WHERE p.Name == "Alphabetter"), 1000),
    (2, (SELECT ProductID FROM Products p WHERE p.Name == "SleepRite"), 10000),
    (3, (SELECT ProductID FROM Products p WHERE p.Name == "Alphabetter"), 5000),
    (4, (SELECT ProductID FROM Products p WHERE p.Name == "Alphabetter"), 4000),
    (5, (SELECT ProductID FROM Products p WHERE p.Name == "ImmuneBoost"), 3000);

/*
1. ImmuneBoost - 100 UnitsProduced from 40 Vitamin C + 1000 Gummy Base
2. SleepRite - 100 UnitsProduced from 20 Melatonin + 1000 Gummy Base
3. Alphabetter - 200 UnitsProduced from 20 each of Vitamins A, B, and C + 2000 Gummy Base
*/
INSERT INTO ProductIngredients (
    ProductID,
    IngredientID,
    QuantityRequired
) VALUES
    (
        (SELECT ProductID FROM Products p WHERE p.Name == "ImmuneBoost"),
        (SELECT IngredientID FROM Ingredients i WHERE i.Name == "Vitamin C"),
        40
    ),
    (
        (SELECT ProductID FROM Products p WHERE p.Name == "ImmuneBoost"),
        (SELECT IngredientID FROM Ingredients i WHERE i.Name == "Gummy Base"),
        1000
    ),
    (
        (SELECT ProductID FROM Products p WHERE p.Name == "SleepRite"),
        (SELECT IngredientID FROM Ingredients i WHERE i.Name == "Gummy Base"),
        1000
    ),
    (
        (SELECT ProductID FROM Products p WHERE p.Name == "SleepRite"),
        (SELECT IngredientID FROM Ingredients i WHERE i.Name == "Melatonin"),
        20
    ),
    (
        (SELECT ProductID FROM Products p WHERE p.Name == "Alphabetter"),
        (SELECT IngredientID FROM Ingredients i WHERE i.Name == "Gummy Base"),
        2000
    ),
    (
        (SELECT ProductID FROM Products p WHERE p.Name == "Alphabetter"),
        (SELECT IngredientID FROM Ingredients i WHERE i.Name == "Vitamin A"),
        20
    ),
    (
        (SELECT ProductID FROM Products p WHERE p.Name == "Alphabetter"),
        (SELECT IngredientID FROM Ingredients i WHERE i.Name == "Vitamin B"),
        20
    ),
    (
        (SELECT ProductID FROM Products p WHERE p.Name == "Alphabetter"),
        (SELECT IngredientID FROM Ingredients i WHERE i.Name == "Vitamin C"),
        20
    );
