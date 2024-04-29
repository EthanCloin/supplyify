I am viewing the database model as _relationships_ between a few core **entities**.

# Entities

- Orders
- Products
- Ingredients

# Relationships

An Order can have one or many related Products

A Product can have one or many related Ingredients

An Ingredient can have zero or many related Products

# Entity Attributes

## Orders

- OrderID (PK)
- OrderProductsID (FK bridging to table relating ProductIDs with the order)
- Status (Open, Procurement, Production, Fulfilled)

## OrderProducts

- OrderProducts (PK)
- OrderID (FK)
- ProductID (FK)
- UnitsRequested

## Products

- ProductID (PK)
- ProductIngredientsID (FK bridging to table relating IngredientIDs with the product)
- Name
- Description
- UnitsPerOrder
- UnitsStocked
- UnitsAllocated
- UnitsFulfilled

## ProductIngredients

- ProductIngredientsID (PK)
- ProductID (FK)
- IngredientID (FK)
- QuantityRequired

## Ingredients

- IngredientsID (PK)
- Name
- Description
- MinimumOrderQuantity
- QuantityStocked
- QuantityAllocated
- QuantityConsumed

# Dummy Data

## Products

Lets say Nutra Factory makes 3 different products:

1. ImmuneBoost - 100 UnitsProduced from 40 Vitamin C + 1000 Gummy Base
2. SleepRite - 100 UnitsProduced from 20 Melatonin + 1000 Gummy Base
3. Alphabetter - 200 UnitsProduced from 20 each of Vitamins A, B, and C + 2000 Gummy Base

## Orders

And they have 5 orders, 2 Open, 1 Procurement, 1 Production, 1 Fulfilled

1. 2 ImmuneBoost and 1 Alphabetter - OPEN
2. 10 SleepRite - OPEN
3. 5 Alphabetter - Procurement
4. 4 Alphabetter - Production
5. 3 ImmuneBoost - Fulfilled

## Ingredients

- Gummy Base
- Vitamin C
- Melatonin
- Vitamin A
- Vitamin B
