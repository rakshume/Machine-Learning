def addition(a, b, c, d):
    """Returns the sum of a and b."""
    return a + b + c + d

addition(2,3,4,5)

def addition_of_numbers(*args):
    """Returns the sum of all arguments."""
    return sum(args)

addition_of_numbers(1, 2, 3, 4, 5)

def substraction_of_numbers(*args):
    """Returns the result of subtracting all arguments from the first."""
    if not args:
        return 0
    result = args[0]
    for num in args[1:]:
        result -= num
    return result

substraction_of_numbers(55,2,5,6,1)

