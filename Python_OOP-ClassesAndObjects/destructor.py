#!/usr/bin/python3
"""What we said about constructors holds true for destructors as well. There
 is no "real" destructor, but something similar, i.e. the method __del__. It
 is called when the instance is about to be destroyed and if there is no other
 reference to this instance. If a base class has a __del__() method, the deri-
ved class's __del__() method, if any, must explicitly call it to ensure proper
 deletion of the base class part of the instance.

The following script is an example with __init__ and __del__:
"""


class Robot():
    def __init__(self, name):
        print(name + " has been created!")

    def __def__(self):
        print("Robot has been destroyed")


if __name__ == "__main__":
    x = Robot("Tik-Tok")
    y = Robot("Jenkins")
    z = x
    print("Deleting x")
    del x
    print("Deleting z")
    del z
    del y
