class Robot:
    def __init__(self, name=None):
        self.name = name

    def say_hi(self):
        if self.name:
            print("Hi, I am {}".format(self.name))
        else:
            print("Hi, I am a robot without a name")

    def set_name(self, name):
            self.name = name

    def get_name(self):
            return self.name


x = Robot()
x.set_name("Henry")
x.say_hi()
y = Robot()
y.set_name(x.get_name())
print(y.get_name())
