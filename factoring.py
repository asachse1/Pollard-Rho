#Name: Adam Sachsel
#Datae: 05/04/2020
#Assn: Pollard_Rho_Factor
#Class: Marron CS441
#Build Inst: Just install the gmpy2 library


import gmpy2
from gmpy2 import *
from random import *
import time

seed(time.time())
#input the modulus as 'n'
def PollardRho(n):
    

    #Setup Variables
    x = mpz(randint(3, n-1))
    y = x
    c = mpz(randint(1, n-1))

    while (True):
        
        x = powmod(x, 2, n)
        y = powmod(x, 2, n)

        p = gcd(abs(y - x), n)
        
        if (p > 1):
            return p

        if (x == y):
            break
    

    return (-1)

def main():

    n = mpz(input("Please enter the modulus: "))
    
    p = PollardRho(n)
    q = mpz(n / p)

    print("One Factor is: ", end = '')
    print(p)

    print("The next Factor is: ", end = '')
    print(q)


if __name__ == '__main__':
    main()