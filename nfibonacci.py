"""
print n number of fibonacci where n is the input number given by user.
"""

def fibonacci(n):
    fib_array = [0,1]
    for i in range(2, n+1):
        fib_array.append(fib_array[i-1] + fib_array[i-2] )
    return fib_array

number_of_fibonacci = int(input("How many fibonacci numbers do you want to print? "))       
print(fibonacci(number_of_fibonacci))