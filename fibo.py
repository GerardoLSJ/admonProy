# Execute with Python 3 or export UTF for Spanish Characters
#
# Team Members:
# Lopez Santibañez Jimenez Luis Gerardo
#
from math import sqrt
def F(n):
    return ((1+sqrt(5))**n-(1-sqrt(5))**n)/(2**n*sqrt(5))

print(F(10))
#Output 55.000000000000014 