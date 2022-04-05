import random


class Operation:
    pass


class Time:
    def __init__(self, l, r):
        self.l = l
        self.r = r

    def __str__(self):
        return "(" + str(self.l) + "*" + str(self.r) + ")"

    def eval(self, env):
        return self.l.eval(env) * self.r.eval(env)


class Plus:
    def __init__(self, l, r):
        self.l = l
        self.r = r

    def __str__(self):
        return "(" + str(self.l) + "+" + str(self.r) + ")"

    def eval(self, env):
        return self.l.eval(env) + self.r.eval(env)


class Const:
    def __init__(self, val):
        self.val = val

    def __str__(self):
        return str(self.val)

    def eval(self, env):
        return self.val


class Var:

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    def eval(self,env):
        return env[self.name]


class RandomInt:
    def __init__(self,min,max):
        self.min = min
        self.max = max

    def __str__(self):
        return "Min: " + str(self.min) + "\nMax " + str(self.max)

    def eval(self):
        return random.choice(range(self.min,self.max))


# e1 = Time(Const(3),Plus(Var("y"),Var("x")))
# e2 = Plus(Time(Const(3),Var("y")),Var("x"))
# e3 = Plus(Var("y"),Var("x"))
#
# print(e1)
# print(e2)
# print(e3)
#
# env = {"x" : 7, "y": 8}
#
# print(e1.eval(env))
# print(e2.eval(env))
# print(e3.eval(env))