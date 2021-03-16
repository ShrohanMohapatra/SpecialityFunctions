from sympy import *
from unittest import TestCase, main
factorial = lambda n: 1 if n == 0 else factorial(n-1)*n
def seriesCoeff(f,x,x0,n):
    if x0 == oo:
        f1 = simplify(f.subs(x,1/x))
        return seriesCoeff(f1,x,0,n)
    r = diff(f,x,n)
    try:
        l = float(limit(r,x,x0))
        return l/factorial(n)
    except TypeError:
        return nan
class testSuite(TestCase):
    def testWithSin(self):
        x = symbols('x')
        f1 = sin(x)
        flag = True
        for n in range(5):
            rn = 0 if n%2 == 0 else (-1)**(int((n-1)/2))/factorial(n)
            flag = flag and N(seriesCoeff(f1,x,0,n)) == rn
        self.assertTrue(flag)
    def testWithCos(self):
        x = symbols('x')
        f1 = cos(x)
        flag = True
        for n in range(5):
            rn = 0 if n%2 == 1 else (-1)**(int(n/2))/factorial(n)
            flag = flag and N(seriesCoeff(f1,x,0,n)) == rn
        self.assertTrue(flag)
    def testWithLog(self):
        x = symbols('x')
        f1 = log(1-x)
        flag = True
        for n in range(5):
            rn = 0 if n==0 else (-1)/n
            flag = flag and N(seriesCoeff(f1,x,0,n)) == rn
        self.assertTrue(flag)
    def testWithGauss(self):
        x = symbols('x')
        f1 = exp(-1/x**2)
        flag = True
        for n in range(5):
            rn = 0 if n%2==1 else (-1)**(int(n/2))/factorial(int(n/2))
            flag = flag and N(seriesCoeff(f1,x,oo,n)) == rn
        self.assertTrue(flag)
    def testWithInvGeo(self):
        x = symbols('x')
        f1 = 1/(1-x)
        flag = True
        for n in range(5):
            rn = 0 if n<1 else -1
            flag = flag and N(seriesCoeff(f1,x,oo,n)) == rn
        self.assertTrue(flag)
    def testWithInvGeo1(self):
        x = symbols('x')
        f1 = 1/(1+x)
        flag = True
        for n in range(5):
            rn = 0 if n<1 else (-1)**(n-1)
            flag = flag and N(seriesCoeff(f1,x,oo,n)) == rn
        self.assertTrue(flag)
    def testWithSinc(self):
        x = symbols('x')
        f1 = sin(x)/x
        flag = True
        for n in range(5):
            rn = 0 if n%2 == 1 else (-1)**(int(n/2))/factorial(n+1)
            flag = flag and N(seriesCoeff(f1,x,0,n)) == rn
        self.assertTrue(flag)
    def testWithInvSinc(self):
        x = symbols('x')
        f1 = sin(x)/x
        flag = True
        for n in range(5):
            flag = flag and (
                N(seriesCoeff(f1,x,oo,n)) == 0 if n == 0 else nan
            )
        self.assertTrue(flag)
    def testWithInvGauss(self):
        x = symbols('x')
        f1 = exp(-1/x**2)
        flag = True
        for n in range(5): flag = flag and N(seriesCoeff(f1,x,0,n)) == 0
        self.assertTrue(flag)
if __name__ == '__main__': main()