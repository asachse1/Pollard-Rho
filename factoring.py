#Name: Adam Sachsel
#Datae: 05/04/2020
#Assn: Pollard_Rho_Factor
#Class: Marron CS441
#Build Inst: Just install the gmpy2 library


import gmpy2
from gmpy2 import *
from random import *
import time
start_time = time.time()

seed(time.time())
#input the modulus as 'n'
def PollardRho(n):
    

    #Setup Variables
    x = mpz(randint(3, n-1))
    y = x
    c = mpz(randint(1, n-1))
    p = 1

    while (True):
        
        x = PollardRhoEquation(x, n, c)
        y = PollardRhoEquation(y, n, c)
        y = PollardRhoEquation(y, n, c)

        p = gcd(abs(y - x), n)
        
        if (p > 1):
            return p
        if(p == n):
            return PollardRho(n)
        if (x == y):
            return PollardRho(n)
    

    return (-1)

def PollardRhoEquation(x, n, c):
    x = (powmod(x, 2, n) + c + n) % n

    return x

def main():

    n = mpz(input("Please enter the modulus: "))
    #n = mpz(132095293493487309427624983656396500488439)
    
    print("\n*** MODULUS *** : ", n)
    p = PollardRho(n)
    q = mpz(n / p)


    if(p != -1):
        print("One Factor is: ", end = '')
        print(p)

        print("The next Factor is: ", end = '')
        print(q)
    else:
        print("No factors Found")
    print("--- %s seconds ---" % (time.time() - start_time), end = "\n\n")


if __name__ == '__main__':
    main()