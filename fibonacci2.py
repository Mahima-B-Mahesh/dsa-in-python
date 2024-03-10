# fibonacci number second method
def fibonacci(n):
    a = 0
    b = 1
    if n < 0:
        print("You entered an invalid number.")
    elif n == 0:
        return a
    elif n == 1:
        return b
    else:
        for i in range(2,n+1):
            c = a + b
            a = b
            b = c
        return b

nth_fibonacci = int(input("what is the index of the fibonacci number you want to print? "))
print(fibonacci(nth_fibonacci))
