#collect base price info
base_price = input("What is the base price of your meal? ")
error_base_price = ("Please enter a number greater than 0")
try:
    base_price = float(base_price)
    if base_price <= 0:
        print(error_base_price)
        exit()
except:
    print(error_base_price)
    exit()

#set tax and tip rate
tax_rate = float(0.085)
tip_rate = float(0.18)

#calculate tax and tip amount
tax_amount = base_price * tax_rate
tip_amount = base_price * tip_rate

#calculate total price
total_price = tax_amount + tip_amount + base_price

#print price breakdown
print(f"Meal: ${base_price}, Tax: ${tax_amount}, Tip: ${tip_amount}, Total: ${total_price}")