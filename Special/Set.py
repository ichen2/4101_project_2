# Set -- Parse tree node strategy for printing the special form set!

from Tree import Nil
from Tree import Closure
from Tree import StrLit
from Tree import Cons
#from Tree import Unspecific
from Print import Printer
from Special import Special

class Set(Special):
    def __init__(self):
        pass
    
    def print(self, t, n, p):
        Printer.printSet(t, n, p)

    def eval(self, exp, env):
        key = exp.getCdr().getCar()
        val = exp.getCdr().getCdr().getCar()
        if key.isSymbol():
            env.assign(key,val)
        return StrLit("no values returned")