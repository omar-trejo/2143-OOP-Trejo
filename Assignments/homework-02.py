"""
Name: Omar Trejo
Email: otrejo0221@my.mwsu.edu
Assignment: Homework 2 - Fraction Class
"""
class fraction(object):
    def gcd(self, n, d):
        while n != d:
            if n > d:
                n = n - d
            else:
                d = d - n
        return n
    def __init__(self,n=None,d=None,w=None):
        self.numerator = n
        self.denominator = d
        self.whole = w
    def __str__(self):
        if self.whole == 0:
            return "%s/%s" % (self.numerator , self.denominator)
        else:
            return "%s %s/%s" % (self.whole, self.numerator , self.denominator)

    def numerator(self,n):
        self.numerator = n 

    def denominator(self,d):
        self.denominator = d

    def whole(self,w):
        self.whole = w

    def __mul__(self,rhs):
        x = self.numerator * rhs.numerator
        y = self.denominator * rhs.denominator
        return fraction(x,y)
    
    def __add__(self,rhs):
        x = self.numerator * rhs.denominator
        x2 = rhs.numerator * self.denominator
        
        Dem = self.denominator * rhs.denominator
        Num = (x + x2) % Dem
        whole = ((x + x2) - Num) / Dem

        gcd1 = self.gcd (Num, Dem)
        finalNum = Num / gcd1
        finalDem = Dem / gcd1

        return fraction (finalNum, finalDem, whole)
    
if __name__ == '__main__':
    a = fraction(1,2)
    b = fraction(1,5)
    c = a + b
    print(c)