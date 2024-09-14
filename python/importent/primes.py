# importent/primes.py
from time import time as tm
from math import isqrt
# from time import sleep as slp

def Is_prime(Input):
    if Input <= 0 or Input == 1:    
        return False
    
    if Input % 2 == 0 and Input != 2 :              # even numbers are not primes
        return False

    for div in range(2, ((isqrt(Input))+1)):        # Chech if the Input is divisible to all the Input the less than it
        if (Input % div) == 0 :                     # If it retutn 0 that mean the munber is divisible , So is not prime.
            return False

    return True                                     # Other wise Input is prime.


def main():
    num_range = int(input("Python script to get a Prime numbers.\nEnter the range >>> "))
    print()
    tm1 = tm()
    i = 0
    for num in range((num_range - 1)):
        if Is_prime((num + 2)):
            i += 1
            znum = str((num + 2)).zfill(len(str(num_range)))
            print(f"{znum} --> prime   | {i}")


    tm2 = tm()
    print (f"time = {tm2 - tm1:.4f} seconds")
    # print("Quit after 60 seconds")
    # slp(60)

if __name__ == '__main__':
    main()