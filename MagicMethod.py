#!/usr/bin/python3

class A:
    def __str__(self):
        return "42"


a = A()
print(repr(a))
print(str(a))
