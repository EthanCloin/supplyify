> problem: how do i handle the assignment of ingredients to products for a specific order?

eg: i have 100 stocked melatonin, and i need 40 for OrderA and 30 for OrderB
i may need to introduce another entity/table?

solution: manage via different 'Quantity' values in the Ingredients and Products tables.
for the melatonin example, if I am processing OrderA, I decrement 40 from `QuantityStocked`, increment
40 to `QuantityAllocated` and once manufacturing is complete, decrement `QuantityAllocated` and increment `QuantityConsumed`.

> problem: how do i manage units between Orders, Products, and Ingredients?

eg: i have an order for productA which would require 2500 units.
This 2500 would be stored in the OrderProducts.UnitsRequested field.

now in the ProductIngredients table, I store the UnitsProduced and QuantityRequired value.
so this junction table really determines the ratio of Ingredient to Product for a given output.

this flexibility might be nice, i don't have to enforce a minimum unitsproduced across the board, it's
particular to each product. or it might be confusing, we will see.

i changed my mind, i want to store the UnitsProduced value at the Product level, keeping it in the junction
table results in repeatedly storing the same value when it will be the same for the product and only vary
on the ingredient level.
