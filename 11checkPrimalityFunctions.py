

def getNumber():
    divisors=0
    num = int(input("Input any number: "))
    for i in range(2, 100):
            if num%i == 2:
                divisors+=1
    print(divisors)

getNumber()
