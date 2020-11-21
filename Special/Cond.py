# Cond -- Parse tree node strategy for printing the special form cond

from Tree import BoolLit
from Tree import Nil
#from Tree import Unspecific
from Print import Printer
from Special import Special

class Cond(Special):
    def __init__(self):
        pass

    def print(self, t, n, p):
        Printer.printCond(t, n, p)
    
    def eval(self, exp, env):
        cond = exp.getCdr()
        while(cond.getCdr() != Nil.getInstance() and cond.getCar().getCar().eval(env) == BoolLit.getInstance(False)):
            cond = cond.getCdr()
        if cond == Nil.getInstance():
            return Nil.getInstance()
        else:
            return cond.getCar().getCdr().getCar().eval(env)
