#!/usr/bin/python
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or not roman_string:
        return 0

    roman_numerals = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
                      'C': 100, 'D': 500, 'M': 1000}

    result = 0
    prev_value = 0

    for char in roman_string:
        current_value = roman_numerals[char]
        result += (
                current_value if current_value <= prev_value
                else current_value - 2 * prev_value
                )

    return result
