#Calculate the nth fibonacci number when n is given, using recursion.

def fibonacci(n):
    assert n >= 0 and int(n) == n , "Fibonacci number cannot be negative or non-integer."
    if n in [0,1]:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2) 
    
number = int(input("What is the index of Fibonacci number you want to print? "))
print(fibonacci(number))