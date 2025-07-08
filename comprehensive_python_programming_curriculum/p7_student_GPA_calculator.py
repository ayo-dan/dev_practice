#set error messages
grade_point_error_message = "Please enter a number between 0.0 and 4.0. "
credit_error_message = "Please enter a whole number that is larger than 0. "

#define get course info function
def get_course():
    course_name = input("What is the name of a course you are taking? Do not type one previously mentioned. ")
    while True:
        course_grade_point = input(f"What is your GPA for {course_name}? Your answer should be between 0.0 and 4.0. ")
        try:
            course_grade_point = float(course_grade_point)
            if course_grade_point < 0 or course_grade_point > 4:
                print(grade_point_error_message)
            else:
                break
        except:
            print(grade_point_error_message)
    while True:
        course_credit = input(f"What are your credit hours for {course_name}? Your answer should be a non negative whole number. ")
        try:
            course_credit = int(course_credit)
            course_credit = float(course_credit)
            if course_credit < 0:
                print(credit_error_message)
            else:
                break
        except:
            print(credit_error_message)
    
    return(course_name, course_grade_point, course_credit)

#calculate course totals (grade_point * credits)
course_1 = get_course()
course_name_1, course_grade_point_1, course_credits_1 = course_1
course_score_1 = course_grade_point_1 * course_credits_1

course_2 = get_course()
course_name_2, course_grade_point_2, course_credits_2 = course_2
course_score_2 = course_grade_point_2 * course_credits_2

course_3 = get_course()
course_name_3, course_grade_point_3, course_credits_3 = course_3
course_score_3 = course_grade_point_3 * course_credits_3

course_4 = get_course()
course_name_4, course_grade_point_4, course_credits_4 = course_4
course_score_4 = course_grade_point_4 * course_credits_4

course_5 = get_course()
course_name_5, course_grade_point_5, course_credits_5 = course_5
course_score_5 = course_grade_point_5 * course_credits_5

#calculate total score, credits, and interpertation of score 
total_course_credts = course_credits_1 + course_credits_2 + course_credits_3 + course_credits_4 + course_credits_5
total_course_score = course_score_1 + course_score_2 + course_score_3 + course_score_4 + course_score_5
gpa = total_course_score / total_course_credts

if gpa == 0:
    interpertation = "ooooof"
elif gpa <= 1:
    interpertation = "Well you are on the right track... I suppose."
elif gpa <= 2: 
    interpertation = "C's get degrees! Lets just hope your employer doesn't need to see a transcript."
elif gpa <= 3:
    interpertation = "If I could reach through the screen and give you a golden star I would"
elif gpa < 4:
    interpertation = "You are super duper smart!"
else:
    interpertation = "You are my sunshine, my very smart and nerdy sunshine :)"

#display GPA end result
print(f"""
*{course_name_1}*   
GPA: {course_grade_point_1}
Credit: {course_credits_1}
Score: {round(course_score_1, 2)}

*{course_name_2}*   
GPA: {course_grade_point_2}
Credit: {course_credits_2}
Score: {round(course_score_2, 2)}

*{course_name_3}*   
GPA: {course_grade_point_3}
Credit: {course_credits_3}
Score: {round(course_score_3, 2)}

*{course_name_4}*   
GPA: {course_grade_point_4}
Credit: {course_credits_4}
Score: {round(course_score_4, 2)}

*{course_name_5}*   
GPA: {course_grade_point_5}
Credit: {course_credits_5}
Score: {round(course_score_5, 2)}

Note from the dean: {interpertation}
""")