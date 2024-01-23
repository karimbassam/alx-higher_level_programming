#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = []

    for i in range(list_length):
        try:
            dividend = my_list_1[i] if i < len(my_list_1) else 0
            divisor = my_list_2[i] if i < len(my_list_2) else 0

            if type(dividend) not in (int, float) or type(divisor) not in (int, float):
                raise TypeError("wrong type")

            if divisor == 0:
                raise ZeroDivisionError("division by 0")

            result.append(dividend / divisor)

        except ZeroDivisionError:
            print("division by 0")
            result.append(0)
        except TypeError:
            print("wrong type")
            result.append(0)

    if len(my_list_1) < list_length or len(my_list_2) < list_length:
        print("out of range")

    return result
