#Calculate the power of a number using recursion.

def power(base, exp):
    assert exp >= 0 and int(exp) == exp , "The exponent must be positive integer only."
    if exp == 0:
        return 1
    elif exp == 1:
        return base
    else:
        return base * power(base,exp-1)

print(power(3,3))