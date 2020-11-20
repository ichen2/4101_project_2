# If -- Parse tree node strategy for printing the special form if

from Tree import BoolLit
from Tree import Nil
from Tree import StrLit
#from Tree import Unspecific
from Print import Printer
from Special import Special

class If(Special):
    def __init__(self):
        pass

    def print(self, t, n, p):
        Printer.printIf(t, n, p)
        
    def eval(self, exp, env):
        condition = exp.getCdr().getCar()
        if condition.eval(env) == BoolLit.getInstance(True):
            return exp.getCdr().getCdr().getCar().eval(env)
        elif not (exp.getCdr().getCdr().getCdr() == Nil.getInstance()):
            return exp.getCdr().getCdr().getCdr().getCar().eval(env)
        else:
            return StrLit("else expression not found")