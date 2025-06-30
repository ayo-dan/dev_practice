#collect and validate commute time
error_commute = "Please enter your commute time in minutes as a number greater than -1."
def validate_commute_input(commute_time):
    try:
        commute_time = float(commute_time)
        if commute_time <= 0:
            print(error_commute)
            exit()
        else:
            return commute_time
    except:
        print(error_commute)
        exit()

morning_commute = input("How many minutes does your morning commute take? ")
morning_commute = validate_commute_input(morning_commute)
evening_commute = input("How many minutes does your evening commute take? ")
evening_commute = validate_commute_input(evening_commute)

#calculate daily and weekly commute time into hours and minutes
daily_commute = round(morning_commute + evening_commute, 2)
weekly_commute = round(daily_commute * 5, 2)
final_hour_commute = round(weekly_commute // 60, 2)
final_minute_commute = round(weekly_commute % 60)

#display commute times
print(f"Daily commute: {daily_commute} minutes, Weekly commute: {weekly_commute} minutes ({final_hour_commute} hours and {final_minute_commute} minutes)")
