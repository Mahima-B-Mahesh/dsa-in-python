#Find the greatest common diviser for the two numbers given.


def euclid_gcd(first,second):
    if second == 0:
        return first
    remainder = first % second
    return euclid_gcd(second,remainder)

number1 = int(input("First number: "))
number2 = int(input("Second number: "))
print(euclid_gcd(number1,number2))