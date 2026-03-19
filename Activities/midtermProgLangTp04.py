first_name = input("Enter Student Name: ")
age = input("Enter Age: ")
quiz_score = input("Enter Quiz Score: ")

PASSING_SCORE = 10

if quiz_score == "":
    status = None
else:
    quiz_score = int(quiz_score)
    quiz_score = float(quiz_score)
    
    if quiz_score >= PASSING_SCORE:
        status = True
    elif quiz_score < PASSING_SCORE:
        status = False

def performance():
    if status is True:
        return "Passed"
    elif status is False:
        return "Failed"
    else:
        return "Has not yet taken the quiz"

print("\n=========================")
print("=    STUDENT REPORT     =")
print("=========================")
print(f"Student Name: {first_name} \nAge: {age} \nQuiz Score: {quiz_score} \nVerdict: {performance()}")
print("=========================")