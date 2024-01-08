#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    # Use the value 0 for missing integers in each tuple
    a = tuple_a + (0, 0)
    b = tuple_b + (0, 0)

    # Return a tuple with the addition of corresponding elements
    result = (a[0] + b[0], a[1] + b[1])
    return result
