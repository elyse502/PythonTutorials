#!/usr/bin/python3

from attribute_tests import A
x = A()
print(f'At first: {x.pub}')
x.pub = x.pub + " and my value can be changed"
print(f"Now: {x.pub}")
print(x._prot)
print(x.__priv)
"""
We get the message "AttributeError: 'A' object has no attribute __priv instead,
 which looks like a "lie". There is such an attribute, but we are told that
 there isn't. This is perfect information hiding. Telling a user that an
 attribute name is private, means that we make some information visible, i.e.
 the existence or non-existence of a private variable.
"""
