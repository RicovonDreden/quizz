#-------------------------Wednesday 21.09.22 Ex 1
# Birthday calculator


"""
 #-------------------Ex 1
from datetime import date

today = date.today()
dob = date(1992, 8, 26)

birthday = date(dob.year, dob.month, dob.day)

print(birthday)

print("Your Birthday is on ", birthday)
"""
#------strptime for creating obj--strf to read out info from ob------------
# #Let´s perform date arithmetic with datetime.timedelta. Adding day m inutes weeks with timedelta
"""
 
from datetime import datetime
mybirthday = "26-08-1992"
format_my_b = datetime.strptime(mybirthday, "%d-%m-%Y")
s = datetime.now()
print(s-format_my_b)
"""
from datetime import datetime
#----------------------------------------------Alpha Project
def new_game():
    guesses = []
    correct_guesses = 0 # set to 0 because we haven´t guessed anything yet
    question_num = 1 # First Q but in order to show index 0 we have to subtract(for loop)

    for key in questions:
        print("----------------------------") # A line break ain´t bad
        print(key)

        for i in options[question_num-1]:
            print(i) #instead of printing all answers we only target the first line answer (index 0)
        guess = input("Enter A, B , C or D:")
        question_num += 1

def check_answer():
    pass
def display_score():
    pass
def play_again():
    pass

questions = {
    "What does timedelta denote?: ": "Answer", #key value pair in Dict of Questions
    "who?: ": "Answer",
    "who?: ": "Answer"}

options = [["A. It denotes a duration", "B. It can also represent the difference bewteen two dates", "C. timedelta(days=3) is a correct Syntax?"],
[" A. Answer", "B. Answer", "C. Answer"],
[" A. Answer", "B. Answer", "C. Answer"]
]

new_game()