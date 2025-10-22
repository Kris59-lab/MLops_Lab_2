def add(*args):
    ''''Returns the sum of all the arguments provided.'''
    return sum(args)


def subtract(*args):
    ''''Return the result of removing all arguments from the first one.'''
    result = args[0]
    for num in args[1:]:
        result -= num
    return result
