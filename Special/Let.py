# Let -- Parse tree node strategy for printing the special form let

from Tree import Nil
from Tree import Environment
from Tree import Cons
from Print import Printer
from Special import Special

class Let(Special):
    def __init__(self):
        pass

    def print(self, t, n, p):
        Printer.printLet(t, n, p)

    def eval(self, exp, env):
        arg = exp.getCdr().getCar()
        expression = exp.getCdr().getCdr().getCar()
        curr = Environment(env)
        arg = self.frame(arg, curr)
        return expression.eval(curr)

    def frame(self, exp, env):
        if exp == Nil.getInstance():
            return Cons(Nil.getInstance(),Nil.getInstance())
        else:
            argument = exp.getCar().getCar()
            expression = exp.getCar().getCdr().getCar()
            rest = exp.getCdr()
            if argument.isSymbol():
                env.define(argument, expression.eval(env))
                return self.frame(rest, env)
            elif argument.isPair():
                return argument.eval(env)
            elif argument == Nil.getInstance():
                return Nil.getInstance()
        return Nil.getInstance() 

        