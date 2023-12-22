#!/usr/bin/python3
'''When we start this program, we can see that it is not possible to
   convert our string x_str, created via str(x), into a Robot object anymore.
'''


class Robot:
    def __init__(self, name, build_year):
        self.name = name
        self.build_year = build_year

    def __repr__(self):
        return "Robot('" + sel.name + "', " + str(self.build_year) + ")"

    def __str__(self):
        return "Name: " + self.name + ", Build Year: " + str(self.build_year)


if __name__ == "__main__":
    x = Robot("marvin", 1979)
    x_str = str(x)
    print(x_str)
    print("Type of x_str: ", type(x_str))
    new = eval(x_str)
    print(new)
    print("Type of new:", type(new))
