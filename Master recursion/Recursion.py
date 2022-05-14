n = int(input()) #taking number from user and typecasting into int

def factorial(n): #defining function factorial
    if n == 0:
        return 1
    else:
        partialAns = factorial(n-1)  
        return n * factorial(n-1)

if(n<0):  # when n is negative, so to stop from infinite loop that is known as base case.
    print("Error")
else: 
    print(factorial(n)) # our factorial answer will be printed on screen
