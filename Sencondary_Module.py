def add(a, b):
    x = a + b
    return x

def sub(a, b):
    x = a - b
    return x

def mult(a, b):
    x = a*b
    return x

def div(a, b):
    if(b == 0):
        return print("Error, cannot divide for zero")
    else:
        x = a/b
        return x