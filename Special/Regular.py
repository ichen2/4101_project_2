# Regular -- Parse tree node strategy for printing regular lists

from Tree import Nil
from Tree import Cons
from Print import Printer
from Special import Special

class Regular(Special):
    def __init__(self):
        pass

    def print(self, t, n, p):
        Printer.printRegular(t, n, p)

    def eval(self, exp, env):
        car = exp.getCar()
        argument = self.evalAll(exp.getCdr(), env)

        while car.isSymbol():
            car = env.lookup(car)
        if car == Nil.getInstance():
            return Nil.getInstance()
        if car.isProcedure():
            return car.apply(argument)
        else:
            return car.eval(env).apply(argument)

    def evalAll(self, exp, env):
        if exp == Nil.getInstance:
            return Cons(Nil.getInstance(), Nil.getInstance())
        else:
            car = exp.getCar()
            cdr = exp.getCdr()
            if car.isSymbol():
                car = env.lookup(car)
            if car == Nil.getInstance():
                return Nil.getInstance()
            return Cons(car.eval(env), self.evalAll(cdr, env)) 
