# Closure -- the data structure for function closures

# Class Closure is used to represent the value of lambda expressions.
# It consists of the lambda expression itself, together with the
# environment in which the lambda expression was evaluated.

# The method apply() takes the environment out of the closure,
# adds a new frame for the function call, defines bindings for the
# parameters with the argument values in the new frame, and evaluates
# the function body.

import sys
from Tree import Node
from Tree import StrLit
from Tree import Environment
from Tree import Nil

class Closure(Node):
    util = None

    @classmethod
    def setUtil(cls, u):
        cls.util = u

    def __init__(self, f, e):
        self.fun = f                    # a lambda expression
        self.env = e                    # the environment in which
                                        # the function was defined

    def getFun(self):
        return self.fun

    def getEnv(self):
        return self.env

    def isProcedure(self):
        return True

    def print(self, n, p=False):
        for _ in range(n):
            sys.stdout.write(' ')
        sys.stdout.write("#{Procedure")
        if self.fun != None:
            self.fun.print(abs(n) + 4)
        for _ in range(abs(n)):
            sys.stdout.write(' ')
        sys.stdout.write(" }\n")
        sys.stdout.flush()

    # TODO: The method apply() should be defined in class Node
    # to report an error.  It should be overridden only in classes
    # BuiltIn and Closure.
    def apply(self, args):
        env = self.getEnv()
        function = self.getFun()
        sym = function.getCar()
        function = function.getCdr().getCar()

        while (not args == Nil.getInstance() and not args.getCar() == Nil.getInstance()):
            env.define(sym.getCar(), args.getCar())
            sym = sym.getCdr()
            args = args.getCdr()
        
        return function.eval(env)
