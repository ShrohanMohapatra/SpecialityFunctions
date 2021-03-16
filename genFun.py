# Exponential generating function
from sympy import *
from unittest import TestCase, main
from random import random
def genFunction(expr,x,n):
    m = symbols('m')
    try:
        return Sum(
            expr.subs(n,m)*(x**m)/factorial(m),(m,0,oo)
        ).doit()
    except:
        return nan
class testSuite(TestCase):
    def test1(self):
        x, n = symbols('x n')
        self.assertTrue(
            genFunction(n**2,x,n) == x*(x+1)*exp(x)
        )
    def test2(self):
        x, n = symbols('x n')
        self.assertTrue(
            genFunction((-1)**n,x,n) == exp(-x)
        )
    def test3(self):
        n = symbols('n')
        k = random()
        self.assertTrue( 
            abs(genFunction(factorial(n),k,n) - N(1/(1-k))) < 10**(-3)
            )
if __name__ == '__main__': main()
