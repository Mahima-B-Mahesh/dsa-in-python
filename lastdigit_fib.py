#to print the last digit of a fibonacci number

def fib_last_digit(n):
    if n < 2:
        return n
    else:
        a, b = 0, 1
        for i in range(1, n):
            a, b = b, (a + b) % 10
        print(b)


n = int(input("Enter the value of n: "))
fib_last_digit(n)
