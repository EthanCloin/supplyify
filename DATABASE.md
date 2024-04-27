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
- Status (Open, In Procurement, In Production, Fulfilled)

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
- UnitsStocked
- UnitsAvailable

## ProductIngredients

- ProductIngredientsID (PK)
- ProductID (FK)
- IngredientID (FK)
- QuantityRequired
- UnitsProduced

## Ingredients

- IngredientsID (PK)
- Name
- Description
- MinimumOrderQuantity
- QuantityStocked
- QuantityAvailable

# thinking out loud

how am i going to organize the relationship bw products and Orders?
specifically, whats the system for quantity?
does the Product manage quantity of UnitsProduced, and the Order specify quantity as ProductQuantity?
i think it's reasonable to let Product manage the UnitsProduced, but let Order include a UnitsRequested

a part of business logic will be comparing Order.UnitsRequested with Product.UnitsProduced to determine the appropriate number of batches to produce for fulfillment.

but actually since UnitsRequested is specific to a given Product, i'll have to keep that data in the OrderProducts row.
