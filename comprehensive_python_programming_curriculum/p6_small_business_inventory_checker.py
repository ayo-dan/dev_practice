#set user inputs in kilograms, US dollars, and lieters
coffee_inventory = "How many kilograms of coffee do you currently have? "
coffee_min = "What is the minimum amount of kilograms of coffee you want to have? "
coffee_max = "What is the maximum amount of kilograms of coffee you want to have? "
coffee_price = float(12)
coffee_weight = "kg"
milk_inventory = "How many lieters of milk do you currently have? "
milk_min = "What is the minimum amount of lieters of milk you want to have? "
milk_max = "What is the maximum amount of lieters of milk you want to have? "
milk_price = float(3)
milk_weight = "l"
error_message = "Pleae enter a non-negative whole number."

#validate user inputs
def validate_prompt(prompt):
    while True:
        value = input(prompt)
        try:
            value = float(value)
            if value >= 0:
                return value
            else:
                print(error_message)
        except:
            print(error_message)

coffee_inventory = validate_prompt(coffee_inventory)
coffee_min = validate_prompt(coffee_min)
coffee_max = validate_prompt(coffee_max)
milk_inventory = validate_prompt(milk_inventory)
milk_min = validate_prompt(milk_min)
milk_max = validate_prompt(milk_max)

#calculate restock status
def restock_check(current, min, max, type, price):
    if current < min:
        restock_status = f"""
Current Inventory: {current}{type}
Current Value: ${current * price}
Restock Status: Reorder Now (below minimum invetory level).
Restock Cost: ${(max - current) * price}
Space Left: {max - current}{type}."""
    elif current == min:
        restock_status = f"""
Current Inventory: {current}{type}
Current Value: ${current * price}
Restock Status: Reorder Now (at minimum invetory level).
Restock Cost: ${(max - current) * price}
Space Left: {max - current}{type}."""
    elif current < max:
        restock_status = f"""
Current Inventory: {current}{type}
Current Value: ${current * price}
Restock Status: Reorder Not Neccessary (at safe invetory level).
Restock Cost: ${(max - current) * price}
Space Left: {max - current}{type}."""
    elif current == max:
        restock_status = f"""
Current Inventory: {current}{type}
Current Value: ${current * price}
Restock Status: Do Not Reorder (at max invetory level).
Restock Cost: ${(current - max) * price}
Space Left: {max - current}{type}."""
    else:
        restock_status = f"""
Current Inventory: {current}{type}
Current Value: ${current * price}
Restock Status: Do Not Reorder (beyond max invetory level).
Restock Cost: ${(current - max) * price}
Space Left: {current - max}{type}."""
    return restock_status

coffee_restock_status = restock_check(coffee_inventory, coffee_min, coffee_max, coffee_weight, coffee_price)
milk_restock_status = restock_check(milk_inventory, milk_min, milk_max, milk_weight, milk_price)

#display inventory analysis
print(f"""
**Coffee Beans** 
{coffee_restock_status}

**Milk***
{milk_restock_status}
""")