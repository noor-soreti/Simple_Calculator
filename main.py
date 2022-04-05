import functions

maxScore = 0
operator_dict = {1: "+", 2: "-", 3: "*"}

file_name = "Score.txt"
file_open = open(file_name, 'a+')
if open(file_name, "r+").readline():
    print("I am happy to see you again.\nYour previous score is ")
else:
    print("Welcome to your Math Game")

continue_program = True

while continue_program:
    functions.myMathTest(maxScore, operator_dict)
    print("Do you want to continue? (Y to continue, any other character to exit)")

    end_program = input()
    if not end_program.lower() == 'y':
        continue_program = False

file_open.close()
