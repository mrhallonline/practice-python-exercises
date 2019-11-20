import math

def getNumber():
#     int(math.sqrt
    divisors=0
    num = int(input("Input any number: "))
    for i in range(2, num, 1):
            if num%i == 0:
                    divisors+=1
    if divisors>=1:
                    print(str(num) + " is not a prime number")
                    
    if divisors == 0:
            print (str(num) + " is a prime number")
getNumber()
