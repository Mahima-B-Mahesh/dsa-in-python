#lcm of two numbers

def gcd(first,second):
    if first == 0:
        return second
    else:
        return gcd(second%first, first)
def lcm(first,second):
    
    return (first // gcd(first,second)) * second

number1 = int(input("First number: "))
number2 = int(input("Second number: "))
print(f"LCM of {number1} and {number2} is {lcm(number1,number2)}")

