# =========================
# Part A — Spot the Bug
# =========================

def add_item(item,cart=[]):
    cart.append(item)
    return cart


print("Part A Output:")
print(add_item("apple"))
print(add_item("banana"))
print(add_item("milk",cart=["bread"]))
print(add_item("eggs"))

# Explanation:
# The default list 'cart=[]' is created only ONCE when the function is defined.
# So the same list is reused across function calls.
#
# Output:
# ['apple']
# ['apple', 'banana']
# ['bread', 'milk']
# ['apple', 'banana', 'eggs']


# ========================
# Part B — Correct Fix
# =========================

def add_item_fixed(item,cart=None):
    if cart is None:
        cart=[]

    cart.append(item)
    return cart


print("\nPart B Output:")
print(add_item_fixed("apple"))
print(add_item_fixed("banana"))

# Now each call gets a fresh list.


# =========================
# Part C — Shopping Cart Program
# =========================

def create_cart(owner,discount=0):
    return {
        "owner":owner,
        "items":[],
        "discount":discount
    }


def add_to_cart(cart, name, price, qty=1):
    item={
        "name":name,
        "price":price,
        "qty":qty
    }

    cart["items"].append(item)


def update_price(price_tuple, new_price):
    try:
        price_tuple[1]=new_price
    except TypeError as e:
        print("\nTuple Error:",e)


def calculate_total(cart):
    total=0

    for item in cart["items"]:
        total+=item["price"]*item["qty"]

    discount_amount=total*(cart["discount"]/100)
    final_total=total-discount_amount

    return final_total


# =========================
# Demo
# =========================

# Creating two independent carts
cart1=create_cart("Aarav",discount=10)
cart2=create_cart("Riya",discount=5)

# Adding items to cart1
add_to_cart(cart1,"Laptop",50000,1)
add_to_cart(cart1,"Mouse",800,2)

# Adding items to cart2
add_to_cart(cart2,"Phone",20000,1)
add_to_cart(cart2,"Charger",1000,1)

# Displaying carts
print("\nCart 1:")
print(cart1)

print("\nCart 2:")
print(cart2)

# Totals
print("\nCart 1 Total:",calculate_total(cart1))
print("Cart 2 Total:",calculate_total(cart2))

# Tuple demo
price_info=("Laptop", 50000)
update_price(price_info, 60000)


# =========================
# Discussion Points
# =========================

# 1. Why is discount=0 safe but cart=[] dangerous?
#===>
# discount=0 is safe because integers are immutable
# cart=[] is dangerous because lists are mutable and shared across calls.


# 2. Difference between rebinding and mutating
#===>
# Rebinding:
# x = [1, 2]
# x = [3, 4]
# Variable now points to a new object.
#
# Mutating:
# x.append(5)
# Original object itself changes.


# 3. Mutable vs Immutable
#===>
# Mutable:
# list, dict, set
#
# Immutable:
# tuple, str, int


# 4. When a list is passed into a function and modified do changes reflect outside?
#===>
# Yes
# Because lists are mutable and functions receive references to the same object.