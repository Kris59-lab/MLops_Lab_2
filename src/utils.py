
def multiply(a : float, b : float) -> float:
    return a * b

def divide(a : float, b : float) -> float:
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    print(f"Dividing {a} by {b}")
    return a / b

def add(*args):
    ''''Returns the sum of all the arguments provided.'''
    return sum(args)


def subtract(*args):
    ''''Return the result of removing all arguments from the first one.'''
    result = args[0]
    for num in args[1:]:
        result -= num
    return result
