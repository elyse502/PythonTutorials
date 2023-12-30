#!/usr/bin/python3
"""Getters and setters are going to be used to protect our objects from assign-
ing bad field values to them or also to provide improved output"""


class Square:
    def __init__(self, height="0", width="0"):
        self.height = height
        self.width = width

    # Defining a getter...
    @property  # This is going to allow us to refer to the fields inside class.
    def height(self):
        print("Retrieving the Height")
        return self.__height
        """This is going to be the function that's called any time a user for
         your Square's is going to require the value for the height now likewi-
        se we are going to create a "setter" and that is going to protect us f-
        rom putting bad data inside of our Squares"""

    # Defining a setter...
    @height.setter
    def height(self, value):
        '''Let's say we want to protect height from receiving a bad value for
        example we want to make sure that the value passed in is a digit. What
         we could do to guarantee that that would work that way is we could s-
        ay:'''
        if value.isdigit():
            self.__height = value
        else:
            print("Please only enter numbers for height")

    '''Doing the same thing for width'''
    # Defining a getter...
    @property  # This is going to allow us to refer to the fields inside class.
    def width(self):
        print("Retrieving the width")
        return self.__width
        """This is going to be the function that's called any time a user for
         your Square's is going to require the value for the width now likewi-
        se we are going to create a "setter" and that is going to protect us f-
        rom putting bad data inside of our Squares"""

    # Defining a setter...
    @width.setter
    def width(self, value):
        '''Let's say we want to protect width from receiving a bad value for
        example we want to make sure that the value passed in is a digit. What
         we could do to guarantee that that would work that way is we could s-
        ay:'''
        if value.isdigit():
            self.__width = value
        else:
            print("Please only enter numbers for width")

    def getArea(self):
        return int(self.__width) * int(self.__height)


def main():
    aSquare = Square()
    height = input("Enter Height: ")
    width = input("Enter Width: ")
    aSquare.height = height
    """What these guys above with "@" do this and the property is it allows us
     to refer to these values (aSquare.height = height) just as height. Othewi-
    se I'd have to come in here (aSquare.height = height(...and put them here))
     But now because we have property set up above in that set up with setter
    we can just refer to them the way that they are..."""
    aSquare.width = width
    print("Height:", aSquare.height)
    print("Width:", aSquare.width)
    print("The Area is:", aSquare.getArea())


main()
