# Project 3

## Web Programming with Python and JavaScript

My implementation of **Study Project 3: Pizza**:
a training project to become more comfortable with Django by building a web application
for handling a pizza restaurant's online orders.
Users are able to browse the restaurant’s menu, add items to their cart, and submit their orders.
The restaurant owners are able to add and update menu items, view orders that have been placed.


### Short description

1. a user can register a new account, log in, log out, change and reset password -
this is implemented using the Django's built-in authentication app in the 'users' app;
2. after logging in, the user sees a greeting and the menu items;
3. when the user clicks on the 'buy' sign next to a menu item,
that item's page will load where he can add the item to his cart either straight ahead or
with selected dish components or additions where applicable;
4. the user can see his cart on the separate page; there he can also submit an order or
cancel all added dishes and start again with an empty cart;
5. the submitted orders are visible in the admin section under
the 'Orders' where the authorized users can see all orders, filter out finished orders,
mark any order as 'finished' after it has been served.

### Notes

After a database has been created, the initial menu can be loaded from the 'load_data.py' file
by executing 'python manage.py shell < load_data.py'.

I have probably chosen a different approach to the models structure than what was expected to keep
things more generic and extensible (for example, categories are not hard coded like Pizza, Salad, etc,
and can be added just like menu items or products).
A category can have:
1. 'components' (for example, pizza toppings) which are included in the price
and need to be specified when an item is selected, or
2. 'additions' (for example, sub additions) which are optional and can (but do not need to) be selected;
To add a new item, one would need to
1. create a new product for an existing category;
2. create new menu items for that product specifying the price for each available size (or leave as None).

Anyway, I'm not quite happy with the outcome as:
1. some non-obvious assumptions have been made when building models and rendering templates,
2. database querying is probably horribly inefficient,
3. design needs a lot of work, etc, but I feel that the goal to get more comfortable with
Django has been achieved and I'm kind of tired of this project, so I'll leave it as it is
and move on to other things.
