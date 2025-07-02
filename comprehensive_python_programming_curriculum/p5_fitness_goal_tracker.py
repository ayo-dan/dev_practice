#set variables for user inputs
step_goal = "What is your step goal for today? "
current_steps = "How many steps have you taken today? "
calorie_goal = "What is your calorie burn goal for today? "
current_calorie = "How many calories have you burned today? "
error_message = "Pleae enter a whole number greater than or equal to 0. "

#define validation function for user inputs
def validate_prompt(prompt):
    while True:
        value = input(prompt)
        try:
            value = int(value)
            if value >= 0:
                return value
            else:
                print(error_message)
        except:
            print(error_message)

#run validation function
current_steps = validate_prompt(current_steps)
step_goal = validate_prompt(step_goal)
current_calorie = validate_prompt(current_calorie)
calorie_goal = validate_prompt(calorie_goal)

#calcualte goal progress and determine associated progress message
step_progress = round((current_steps / step_goal) * 100, 2)
step_remaining = step_goal - current_steps
calorie_progress = round((current_calorie / calorie_goal) * 100, 2)
calorie_remaining = calorie_goal - current_calorie

def progress_message(progress):
    if progress <= 20:
        progress_message = "I'm surprised you're even checking your progress at this point..."
    elif progress <= 40:
        progress_message = "First steps! Keep it up and you'll hit your goal at some point."
    elif progress <= 60:
        progress_message = "I give you an approving nod and the promise of a high five if you keep it up."
    elif progress <= 80:
        progress_message = "Nice, real real nice."
    elif progress < 100:
        progress_message = "Here's your high five. Proud of you ;)"
    elif progress == 100:
        progress_message = "Time to set higher goals, because you crushed this one with mathmatical percision."
    else:
        progress_message = "Can I be your plus one to Mt. Olympus?"
    return progress_message

step_progress_message = progress_message(step_progress)
calorie_progress_message = progress_message(calorie_progress)

#display goal progress
print(f"""
Steps Taken Goal: {current_steps}/{step_goal} ({step_progress}% complete, {step_remaining} remaining)
{step_progress_message} 

Calorie Burn Goal: {current_calorie}/{calorie_goal} ({calorie_progress}% complete, {calorie_remaining} remaining)
{calorie_progress_message}
""")