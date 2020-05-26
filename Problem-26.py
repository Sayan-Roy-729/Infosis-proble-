# A vendor at a food court is in the process of automating his order management system.
# The vendor serves the following menu – Veg Roll, Noodles, Fried Rice and Soup and also
# maintains the quantity available for each item. The customer can order any combination of
# items. The customer is provided the item if the requested quantity of item is available with the
# vendor.

# Write a python program which implements the following functions.

#       place_order(*item_tuple):       This function accepts the order placed by the customer. Consider it
# to be a variable length argument as each customer may have a different order.
# The function should check whether the items requested are present in the vendor’s menu and if
# so, it should check whether the requested quantity is available for each by invoking the
# check_quantity_available() method.

#       The function should display appropriate messages for each item in the order for the below
# scenarios:
# 1. When the requested item is not available in vendor’s menu, display <Item Name> is not
# available
# 2. When the quantity requested by the customer is not available, display <Item Name>
# stock is over
# 3. When the requested quantity of the item is available with the vendor, display <Item
# Name> is available

#       check_quantity_available(index,quantity_requested):         This function should check whether the
# requested quantity of the specified item is available. If so, it should reduce the quantity
# requested from the quantity available for that item and return True. Otherwise, it should return
# False.

def place_order(order_item, order_quantity):

    menu = ("Veg Roll", "Noodles", "Fried Rice" , "Soup")
    quantity = [2,200,3,0]

    for order in order_item:
        if order in menu:
            call_function = check_quantity_available( menu, quantity, order,  order_quantity)
            if call_function:
                print(f"{order} is available\n")
            else:
                print(f"{order} stock is over")
        else:
            print(f"{order} is not available")



def check_quantity_available(menu, quantity, order, order_quantity):

    menu_index = menu.index(order)
    available_quantity = quantity[menu_index]
    order_item_index = order_item.index(order)
    order_quantity_order = order_quantity[order_item_index]
    if order_quantity_order <= available_quantity:
        quantity[menu_index] = quantity[menu_index] - order_quantity_order
        return True
    else:
        return False 

        

if __name__ == "__main__":
    order_item = ["Fried Rice", "Soup"]
    order_quantity = [2, 1]
    place_order(order_item, order_quantity)
   