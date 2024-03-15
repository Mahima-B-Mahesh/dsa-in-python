#Calculate the factorial of number n given , using recursion

def factorial(n):
    assert n >= 0 and int(n) == n, "The number must be a positive integer only."
    if n in [0,1]:
        return n
    else:
        return n * factorial(n-1)
    
number = int(input("Enter the number: "))
print(factorial(number))