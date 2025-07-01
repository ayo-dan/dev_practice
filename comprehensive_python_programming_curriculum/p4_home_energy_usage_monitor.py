#set user inputs
error_input = "Please enter a valid number."
refrigerator_energy = "how many watts does your refrigerator use? "
refrigerator_time = "how many hours does your refrigerator run? "
tv_energy = "how many watts does your tv use? "
tv_time = "how many hours does your tv run? "
light_energy = "how many watts does your light use? "
light_time = "how many hours does your light run? "

#set validation function for user inputs
def validate_energy_input(energy_prompt):
    while True:
        appliance_input = input(energy_prompt)
        try:
            appliance_input = float(appliance_input)
            if appliance_input >= 0:
                return appliance_input
        except:
            print(error_input)

#run validation function on user inputs
refrigerator_energy = validate_energy_input(refrigerator_energy)
refrigerator_time = validate_energy_input(refrigerator_time)
tv_energy = validate_energy_input(tv_energy)
tv_time = validate_energy_input(tv_time)
light_energy = validate_energy_input(light_energy)
light_time = validate_energy_input(light_time)

#set multiplication function for energy usage and time
def determine_energy_usage(energy_input, time_input):
    kwh_usage = (energy_input * time_input) / 1000
    return kwh_usage

refrigerator_kwh = determine_energy_usage(refrigerator_energy, refrigerator_time)
tv_kwh = determine_energy_usage(tv_energy, tv_time)
light_kwh = determine_energy_usage(light_energy, light_time)

#calculate total daily and monthly energy usage and cost ($0.12 per kWh)
daily_total = refrigerator_kwh + tv_kwh + light_kwh
round_daily_total = round(daily_total, 2)
daily_total_cost = daily_total * 0.12
round_daily_total_cost = round(daily_total_cost, 2)
monthly_total = daily_total * 30
round_monthly_total = round(monthly_total, 2)
monthly_total_cost = monthly_total * 0.12
round_monthly_total_cost = round(monthly_total_cost, 2)

#display results
print(f"Refrigerator: {refrigerator_kwh}kWh, TV: {tv_kwh}kWh, Light: {light_kwh}kWh. Total: {round_daily_total}kWh daily, {round_monthly_total}kWh monthly, Est. cost: ${round_monthly_total_cost}")