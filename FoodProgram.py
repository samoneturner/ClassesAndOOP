import FoodClass as fc

# this dictionary represents transactions. The key of the dictionary is the transaction identifier.
# The Value of the dictionary is a list. The elements in each list are -
# ['Date', 'Name of item', 'Cost', 'customerid' ]

dict = {
    "trans1": ["2/15/2023", "The Lone Patty", 17, 569],
    "trans2": ["2/15/2023", "The Octobreakfast", 18, 569],
    "trans3": ["2/15/2023", "The Octoveg", 16, 570],
    "trans4": ["2/15/2023", "The Octoburger", 20, 570],
}

order_total = 0


# customerid = 570
# name = "Danni Sellyar"
# address = "97 Mitchell Way Hewitt Texas 76712"
# email = "dsellyarft@gmpg.org"
# phone = "254-555-9362"
# member_status = False

customerid = 569
name = "Aubree Himsworth"
address = "1172 Moulton Hill Waco Texas 76710"
email = "ahimsworthfs@list-manage.com"
phone = "254-555-2273"
member_status = True

customer1 = fc.Customer(customerid, name, address, email, phone, member_status)

print("Customer Name: ", customer1.get_name())
print("Phone: ", customer1.get_phone())
for key in dict:
    if dict[key][3] == customerid:
        date = dict[key][0]
        item_name = dict[key][1]
        cost = dict[key][2]
        order_total += cost
        print(f"Order Item: {item_name}  Price: ${cost:,.2f}")
print(f"Total Cost: ${order_total:,.2f}")
if customer1.get_member_status() == True:
    member_discount = order_total * 0.20
    order_total *= 0.80
    print(f"Member Discount: ${member_discount:,.2f}")
    print(f"Total Cost after discount: ${order_total:,.2f}")
else:
    print(f"Total Cost: ${order_total:,.2f}")
