#!/usr/bin/python3
"""Now comes the point which frightens some traditional OOPistas out of their
 wits: Imagine "OurAtt" has been used as an integer. Now, our class has to en-
sure that "OurAtt" has to be a value between 0 and 1000? Without property, this
 is really a horrible scenario! Due to properties it's easy: We create a prop-
erty version of "OurAtt".
"""


class OurClass:
    def __init__(self, a):
        self.OurAtt = a

    @property
    def OurAtt(self):
        return self.__OurAtt

    @OurAtt.setter
    def OurAtt(self, val):
        if val < 0:
            self.__OurAtt = 0
        elif val > 1000:
            self.__OurAtt = 1000
        else:
            self.__OurAtt = val


x = OurClass(10)
print(x.OurAtt)
x.OurAtt = -1
print(x.OurAtt)
x.OurAtt = 1001
print(x.OurAtt)
"""This is great, isn't it? You can start with the simplest implementation im-
aginable, and you are free to later migrate to a property version without hav-
ing to change the interface! So properties are not just a replacement for get-
ters and setters!

Something else you might have already noticed: For the users of a class, prop-
erties are syntactically identical to ordinary attributes.
"""
