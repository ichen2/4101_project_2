# BuiltIn -- the data structure for built-in functions

# Class BuiltIn is used for representing the value of built-in functions
# such as +.  Populate the initial environment with
# (name, BuiltIn(name)) pairs.

# The object-oriented style for implementing built-in functions would be
# to include the Python methods for implementing a Scheme built-in in the
# BuiltIn object.  This could be done by writing one subclass of class
# BuiltIn for each built-in function and implementing the method apply
# appropriately.  This requires a large number of classes, though.
# Another alternative is to program BuiltIn.apply() in a functional
# style by writing a large if-then-else chain that tests the name of
# the function symbol.

import sys
from Parse import *
from Tree import Node
from Tree import BoolLit
from Tree import IntLit
from Tree import StrLit
from Tree import Ident
from Tree import Nil
from Tree import Cons
from Tree import TreeBuilder
#from Tree import Unspecific

class BuiltIn(Node):
    env = None
    util = None

    @classmethod
    def setEnv(cls, e):
        cls.env = e

    @classmethod
    def setUtil(cls, u):
        cls.util = u

    def __init__(self, s):
        self.symbol = s                 # the Ident for the built-in function

    def getSymbol(self):
        return self.symbol

    def isProcedure(self):
        return True

    def print(self, n, p=False):
        for _ in range(n):
            sys.stdout.write(' ')
        sys.stdout.write("#{Built-In Procedure ")
        if self.symbol != None:
            self.symbol.print(-abs(n) - 1)
        sys.stdout.write('}')
        if n >= 0:
            sys.stdout.write('\n')
            sys.stdout.flush()

    # TODO: The method apply() should be defined in class Node
    # to report an error.  It should be overridden only in classes
    # BuiltIn and Closure.
    def apply(self, args):
        print("fdsddf")
        #return StrLit("Error: BuiltIn.apply not yet implemented")

        ## The easiest way to implement BuiltIn.apply is as an
        ## if-then-else chain testing for the different names of
        ## the built-in functions.  E.g., here's how load could
        ## be implemented:
 
        # if name == "load":
        #     if not arg1.isString():
        #         self._error("wrong type of argument")
        #         return Nil.getInstance()
        #     filename = arg1.getStrVal()
        #     try:
        #         scanner = Scanner(open(filename))
        #         builder = TreeBuilder()
        #         parser = Parser(scanner, builder)

        #         root = parser.parseExp()
        #         while root != None:
        #             root.eval(BuiltIn.env)
        #             root = parser.parseExp()
        #     except IOError:
        #         self._error("could not find file " + filename)
        #     return Nil.getInstance()  # or Unspecific.getInstance()
        
        # this may or may not work

        # get args (arg 1 is the car, arg 2 is the car of the cdr)
        if args == None:
            return Nil.getInstance()
        name = self.symbol.getName()
        car = args.getCar()
        if car.isNull():
            car = Nil.getInstance()
        cdr = args.getCdr()
        # if there is no arg 2, just set it to nil
        if cdr.isNull():
            cdr = Nil.getInstance()
        # otherwise arg2 is the car of the cdr
        else:
            cdr = cdr.getCar()
        
        if name == "b+":
            if car.isNumber() and cdr.isNumber():
                print("sdhfahl")
                return IntLit(car.getVal() + cdr.getVal())
            else:
                print("Invalid arguments for b+")
                return StrLit("")