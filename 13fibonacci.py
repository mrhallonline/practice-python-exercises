# Write a program that asks the user how many Fibonacci numbers to generate and then generates them. Take this opportunity to think about how you can use functions. Make sure to ask the user to enter the number of numbers in the sequence to generate.(Hint: The Fibonacci sequence is a sequence of numbers where the next number in the sequence is the sum of the previous two numbers in the sequence. The sequence looks like this: 1, 1, 2, 3, 5, 8, 13, …)

        # fibSum = sum(fibList)
def fibGenerator(fibNumber):
        if (fibNumber == 0):
            fibList = []
        elif (fibNumber == 1):
            fibList = [1]
        elif (fibNumber == 2): 
            fibList = [1,1]
        elif (fibNumber>=3):
            fibList = [1,1]    
            for i in range (fibNumber-2):
                fibList.append(fibList[-1]+fibList[-2])
        print(fibList)

fibNumber = int(input("How many Fibonacci numbers should I generate?: "))
fibGenerator(fibNumber)