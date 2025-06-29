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
base_price = round(base_price, 2)

#set tax and tip rate
tax_rate = float(0.085)
tip_rate = float(0.18)

#calculate rounded tax and tip amount
tax_amount = base_price * tax_rate
rounded_tax_amount = round(tax_amount, 2)
tip_amount = base_price * tip_rate
rounded_tip_amount = round(tip_amount, 2)

#calculate total price
total_price = rounded_tax_amount + rounded_tip_amount + base_price

#print price breakdown
print(f"Meal: ${base_price}, Tax: ${rounded_tax_amount}, Tip: ${rounded_tip_amount}, Total: ${total_price}")
