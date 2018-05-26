from orders import models


# PIZZA
REGULAR_PIZZAS = [
    ("Cheese", 0, (11.70, 16.45)),
    ("Cheese", 1, (12.70, 18.45)),
    ("Cheese", 2, (14.20, 20.45)),
    ("Cheese", 3, (15.20, 22.45)),
    ("Special", 0, (16.75, 24.45))
]
for r in REGULAR_PIZZAS:
    item = models.Pizza(title=r[0], toppings_number=r[1], size="small", kind="regular", price=r[2][0])
    item.save()
    item = models.Pizza(title=r[0], toppings_number=r[1], size="large", kind="regular", price=r[2][1])
    item.save()

SICILIAN_PIZZAS = [
    ("Cheese", 0, (22.45, 35.70)),
    ("Cheese", 1, (24.45, 37.70)),
    ("Cheese", 2, (26.45, 39.70)),
    ("Cheese", 3, (27.45, 41.70)),
    ("Special", 0, (28.45, 42.70))
]
for r in SICILIAN_PIZZAS:
    item = models.Pizza(title=r[0], toppings_number=r[1], size="small", kind="sicilian", price=r[2][0])
    item.save()
    item = models.Pizza(title=r[0], toppings_number=r[1], size="large", kind="sicilian", price=r[2][1])
    item.save()

TOPPINGS = """Pepperoni
Sausage
Mushrooms
Onions
Ham
Canadian Bacon
Pineapple
Eggplant
Tomato & Basil
Green Peppers
Hamburger
Spinach
Artichoke
Buffalo Chicken
Barbecue Chicken
Anchovies
Black Olives
Fresh Garlic
Zucchini"""
for r in TOPPINGS.split("\n"):
    item = models.PizzaTopping(title=r)
    item.save()


# SUBS
SUBS = [
    ("Cheese", 6.50, 7.95),
    ("Italian", 6.50, 7.95),
    ("Ham + Cheese", 6.50, 7.95),
    ("Meatball", 6.50, 7.95),
    ("Tuna", 6.50, 7.95),
    ("Turkey", 7.50, 8.50),
    ("Chicken Parmigiana", 7.50, 8.50),
    ("Eggplant Parmigiana", 6.50, 7.95),
    ("Steak", 6.50, 7.95),
    ("Steak + Cheese", 6.95, 8.50),
    ("Sausage, Peppers & Onions", None, 8.50),
    ("Hamburger", 4.60, 6.95),
    ("Cheeseburger", 5.10, 7.45),
    ("Fried Chicken", 6.95, 8.50),
    ("Veggie", 6.95, 8.50)
]
for r in SUBS:
    if r[1] is not None:
        item = models.Sub(title=r[0], size="small", price=r[1])
        item.save()
    if r[2] is not None:
        item = models.Sub(title=r[0], size="large", price=r[2])
        item.save()

SUBADDITIONS = [
    ("Mushrooms", 0.5),
    ("Green Peppers", 0.5),
    ("Onions", 0.5),
    ("Extra Cheese", 0.5)
]
for r in SUBADDITIONS:
    item = models.SubAddition(title=r[0], price=r[1])
    item.save()


# OTHER
PASTAS = [
    ("Baked Ziti w/Mozzarella", 6.50),
    ("Baked Ziti w/Meatballs", 8.75),
    ("Baked Ziti w/Chicken", 9.75)
]
for r in PASTAS:
    item = models.Pasta(title=r[0], price=r[1])
    item.save()

SALADS = [
    ("Garden Salad", 6.25),
    ("Greek Salad", 8.25),
    ("Antipasto", 8.25),
    ("Salad w/Tuna", 8.25)
]
for r in SALADS:
    item = models.Salad(title=r[0], price=r[1])
    item.save()

DINNERPLATTERS = [
    ("Garden Salad", 35.00, 60.00),
    ("Greek Salad", 45.00, 70.00),
    ("Antipasto", 45.00, 70.00),
    ("Baked Ziti", 35.00, 60.00),
    ("Meatball Parm", 45.00, 70.00),
    ("Chicken Parm", 45.00, 80.00)
]
for r in DINNERPLATTERS:
    if r[1] is not None:
        item = models.DinnerPlatter(title=r[0], size="small", price=r[1])
        item.save()
    if r[2] is not None:
        item = models.DinnerPlatter(title=r[0], size="large", price=r[2])
        item.save()
