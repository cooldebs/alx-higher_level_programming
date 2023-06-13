#!/usr/bin/python3
"""Defines MyInt class"""


class MyInt(int):
    """Represents MyInt class
    MyInt is a rebel
    MyInt has == and != operators inverted
    """
    def __eq__(self, value):
        """Override == opeartor with != behavior"""
        return self.real != value

    def __ne__(self, value):
        """Override != opeartor with == behavior"""
        return self.real == value
