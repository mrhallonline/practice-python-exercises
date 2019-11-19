# Write a program that asks the user how many Fibonacci numbers to generate and then generates them. Take this opportunity to think about how you can use functions. Make sure to ask the user to enter the number of numbers in the sequence to generate.(Hint: The Fibonacci sequence is a sequence of numbers where the next number in the sequence is the sum of the previous two numbers in the sequence. The sequence looks like this: 1, 1, 2, 3, 5, 8, 13, …)

def fibGenerator(fibNumber):
    fibList = [1]
    for i in range (fibNumber):
        fibSum = sum(fibList)
        if (fibSum <= 1):
            fibList.append(1)
        else:
            fibList.append(fibList[-1]+fibList[-2])
    print(fibList)

fibNumber = int(input("How many Fibonacci numbers should I generate?: "))
fibGenerator(fibNumber)