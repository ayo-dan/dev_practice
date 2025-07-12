#set variables
after_tax_income = "What is your after tax monthly income? "
needs = float(0.5)
actual_needs = "How much do you spend monthly on your needs? "
wants = float(0.3)
actual_wants = "How much do you spend monthly on your wants? "
savings = float(0.2)
actual_savings = "How much do you contribute monthly to your savings? "
error_message = "Please enter a numnber. It can include a decimal point."

#define function to check if inputs are floats
def user_prompt(prompt):
    while True:
        value = input(prompt)
        try:
            value = float(value)
            return(value)
        except:
            print(error_message)

#run user_prompt function
after_tax_income = user_prompt(after_tax_income)
actual_needs = user_prompt(actual_needs)
actual_wants = user_prompt(actual_wants)
actual_savings = user_prompt(actual_savings)

#calculate target and variance
target_needs = after_tax_income * needs
variance_needs = actual_needs - target_needs
target_wants = after_tax_income * wants
variance_wants = actual_wants - target_wants
target_savings = after_tax_income * savings
variance_savings = actual_savings - target_savings

leftover = variance_needs + variance_wants + variance_savings
if leftover > 0:
    leftover_reccomendation = "You can spent more of your income."
elif leftover < 0:
    leftover_reccomendation = "You need to save more of your income."
else:
    leftover_reccomendation = "You have met your budget requirements."

#define function to determine recomendation based of variance from target
def conclusion(actual, target):
    if actual > target:
        conclusion = "Under budget"
    elif actual < target:
        conclusion = "Over budget"
    else:   
        conclusion = "At budget"
    return conclusion

#run recomendation function
needs_conclusion = conclusion(actual_needs, target_needs)
wants_conclusion = conclusion(actual_wants, target_wants)
savings_conclusion = conclusion(actual_savings, target_savings)

#display budget planner output
print(f"""
Here is your budget analysis based off a ${after_tax_income} monthly after tax income:
      
**Needs - 50% of Income**
Actual: {actual_needs}
Target: {target_needs}
Conclusion: {variance_needs} {needs_conclusion}
      
**Wants - 30% of Income**
Actual: {actual_wants}
Target: {target_wants}
Conclusion: {variance_wants} {wants_conclusion}

*Savings - 20% of Income**
Actual: {actual_savings}
Target: {target_savings}
Conclusion: {variance_savings} {savings_conclusion}

**Net**
You have {leftover} leftover in your budget. {leftover_reccomendation}

""")