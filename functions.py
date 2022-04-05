import random
import classes


def myMathTest(maxScore, operator_dict):
    ran_val = classes.RandomInt(1,11)
    ran_op = random.choice(range(1,len(operator_dict)+1))

    env = {"x": ran_val.eval(), "y": ran_val.eval()}

    print("Evaluate the following equation:")
    print(env["x"], operator_dict[ran_op], env["y"])

    if ran_op == 1:
        e1 = classes.Plus(classes.Var("x"), classes.Var("y"))
        print(e1)
    elif ran_op == 2:
        e1 = 2
    else:
        e1 = classes.Time(classes.Var("x"), classes.Var("y"))
        print(e1)

    user_input = input()
    while not user_input.isnumeric():
        print("Whoops... only numeric values please")
        user_input = input()

    if int(user_input) == e1.eval(env):
        print("Congratulations! You're a Pro")
    else:
        print("The correct answer is " + str(e1.eval(env)) + " Let's try another question")


def EndProgram():
    pass