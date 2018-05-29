from orders import models


CATEGORIES = [
    ("Regular Pizza", "primary"),
    ("Sicilian Pizza", "primary"),
    ("Toppings", "supplementary"),
    ("Subs", "primary"),
    ("Sub Extras", "supplementary"),
    ("Pasta", "primary"),
    ("Salads", "primary"),
    ("Dinner Platters", "primary")
]
for r in CATEGORIES:
    item = models.Category(name=r[0], kind=r[1])
    item.save()

SIZES = ["large", "small"]
for r in SIZES:
    item = models.ProductSize(name=r)
    item.save()

SMALL = models.ProductSize.objects.get(name="small")
LARGE = models.ProductSize.objects.get(name="large")


# PIZZA
REGULAR_PIZZAS = [
    ("Cheese", 11.70, 16.45, 0),
    ("1 topping", 12.70, 18.45, 1),
    ("2 toppings", 14.20, 20.45, 2),
    ("3 toppings", 15.20, 22.45, 3),
    ("Special", 16.75, 24.45, 0)
]
cat = models.Category.objects.get(name="Regular Pizza")
extras_category = models.Category.objects.get(name="Toppings")
for r in REGULAR_PIZZAS:
    item = models.Product(name=r[0], size=SMALL, category=cat, extras_category=extras_category, extras_amount=r[3], price=r[1])
    item.save()
    item = models.Product(name=r[0], size=LARGE, category=cat, extras_category=extras_category, extras_amount=r[3], price=r[2])
    item.save()



SICILIAN_PIZZAS = [
    ("Cheese", 22.45, 35.70, 0),
    ("1 item", 24.45, 37.70, 1),
    ("2 items", 26.45, 39.70, 2),
    ("3 items", 27.45, 41.70, 3),
    ("Special", 28.45, 42.70, 0)
]
cat = models.Category.objects.get(name="Sicilian Pizza")
extras_category = models.Category.objects.get(name="Toppings")
for r in SICILIAN_PIZZAS:
    item = models.Product(name=r[0], size=SMALL, category=cat, extras_category=extras_category, extras_amount=r[3], price=r[1])
    item.save()
    item = models.Product(name=r[0], size=LARGE, category=cat, extras_category=extras_category, extras_amount=r[3], price=r[2])
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
cat = models.Category.objects.get(name="Toppings")
for r in TOPPINGS.split("\n"):
    item = models.Product(name=r, category=cat)
    item.save()



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
cat = models.Category.objects.get(name="Subs")
extras_category = models.Category.objects.get(name="Sub Extras")
for r in SUBS:
    if r[1] is not None:
        item = models.Product(name=r[0], size=SMALL, category=cat, extras_category=extras_category, price=r[1])
        item.save()
    if r[2] is not None:
        item = models.Product(name=r[0], size=LARGE, category=cat, extras_category=extras_category, price=r[2])
        item.save()



SUBADDITIONS = [
    ("Mushrooms", 0.5),
    ("Green Peppers", 0.5),
    ("Onions", 0.5),
    ("Extra Cheese", 0.5)
]
cat = models.Category.objects.get(name="Sub Extras")
for r in SUBADDITIONS:
    item = models.Product(name=r[0], category=cat, price=r[1])
    item.save()



PASTAS = [
    ("Baked Ziti w/Mozzarella", 6.50),
    ("Baked Ziti w/Meatballs", 8.75),
    ("Baked Ziti w/Chicken", 9.75)
]
cat = models.Category.objects.get(name="Pasta")
for r in PASTAS:
    item = models.Product(name=r[0], category=cat, price=r[1])
    item.save()



SALADS = [
    ("Garden Salad", 6.25),
    ("Greek Salad", 8.25),
    ("Antipasto", 8.25),
    ("Salad w/Tuna", 8.25)
]
cat = models.Category.objects.get(name="Salads")
for r in SALADS:
    item = models.Product(name=r[0], category=cat, price=r[1])
    item.save()




DINNERPLATTERS = [
    ("Garden Salad", 35.00, 60.00),
    ("Greek Salad", 45.00, 70.00),
    ("Antipasto", 45.00, 70.00),
    ("Baked Ziti", 35.00, 60.00),
    ("Meatball Parm", 45.00, 70.00),
    ("Chicken Parm", 45.00, 80.00)
]
cat = models.Category.objects.get(name="Dinner Platters")
for r in SUBS:
    if r[1] is not None:
        item = models.Product(name=r[0], size=SMALL, category=cat, price=r[1])
        item.save()
    if r[2] is not None:
        item = models.Product(name=r[0], size=LARGE, category=cat, price=r[2])
        item.save()
