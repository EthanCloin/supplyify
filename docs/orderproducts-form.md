i want this form to support adding/removing products on an order being created.

i want the form to supply a dropdown of available products on each form.
dropdown should disinclude products already selected.

## getting the product dropdown

i send a request to server asking for all products.
how does [htmx handle validation](https://htmx.org/docs/#validation)?
it fires an event that i can hook into via `hx-on` and add the check.

i should have that function collect orderproductids already present in the form
and ensure....well. i don't really need a validation step i need a step before the user enters anything
to make sure my dropdown is correctly populated. but maybe same idea and just run in on the user entering the
input field.

i should have the full list of products held by my create-form element in a single datalist.
then when one is selected i toggle the disabled attr.
