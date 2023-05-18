#!/usr/bin/python3
def roman_to_int(roman_string):
    """ a function that converts a Roman numeral to an integer."""
    if not roman_string or type(roman_string) != str:
        return (0)
    result = 0
    digits = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
    for roman in reversed(roman_string):
        total = digits[roman]
        result += total if result < total * 5 else -total
    return (result)
