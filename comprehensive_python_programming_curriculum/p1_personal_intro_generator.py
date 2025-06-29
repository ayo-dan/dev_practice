#collect info on user
name = input("What is your name? ")

age = input("How old are you? ")
age_error = ("Please enter a number that is greater than 0. ")
try:
    age = int(age)
    if age <= 0:
        print(age_error)
        exit()
except:
    print(age_error)
    exit()

hobby = input("What is your favorite hobby? ")

#print statement containing collection info
print(f"Hello! My name is {name}, I am {age} years old, and I love {hobby}")