# Check Pass or Fail

def get_student_data():
    name = input("What is your name? ")
    grade = int(input("Enter Your Score: "))
    return name, grade 


def check_pass_fail(score):
    if score >= 75:
        return "Passed!"
    else:
        return "Failed!"


def show_result(name, score, grade):
    print("=-=-= Result =-=-=")
    print("Name:",name)
    print("Score:",grade)
    print("Pass or Fail:",score)


# main program
name, grade = get_student_data()
score = check_pass_fail(grade)
show_result(name, score, grade)