# Capitalize a given string using recursion

def capitalize(arr : str):
    result = ""
    if len(arr) == 0:
        return result
    result += arr[0][0].upper() + arr[0][1:]
    return result + capitalize(arr[1:])

print(capitalize("MAhima"))