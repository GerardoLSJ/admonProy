# Execute with Python 3 or export UTF for Spanish Characters
#
# Team Members:
# Gonzalez Valdez Bryan
# Lopez Santibanez Jimenez Luis Gerardo
# Hernandez Garcia Israel
#
from math import sqrt
print("Dada la funcion f=(1+5^(1/2))^n-(1-5^(1/2))^n)/(2^n x 5^(1/2))\n")
print("y numero n, este programa obtiene la f(n) asociada.\n")
def F(n):
    return ((1+sqrt(5))**n-(1-sqrt(5))**n)/(2**n*sqrt(5))

print("con n=10\nf=")
print(F(10))
#Output 55.000000000000014 
