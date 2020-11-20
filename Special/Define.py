# Define -- Parse tree node strategy for printing the special form define

from Tree import Ident
from Tree import StrLit
from Tree import Nil
from Tree import Cons
from Tree import Closure
#from Tree import Void
from Print import Printer
from Special import Special

class Define(Special):
    def __init__(self):
        pass

    def print(self, t, n, p):
        Printer.printDefine(t, n, p)

    def eval(self, exp, env):
        key = exp.getCdr().getCar()
        val = exp.getCdr().getCdr().getCar()
        # if defining a variable
        if key.isSymbol():
            env.define(key,val)
        # if defining a function
        else:
            func = Closure(Cons(exp.getCdr().getCar().getCdr(),exp.getCdr().getCdr()),env)
            env.define(key.getCar(),func)
        return StrLit("no values returned")
