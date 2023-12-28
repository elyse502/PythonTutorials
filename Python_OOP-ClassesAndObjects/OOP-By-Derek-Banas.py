#!/usr/bin/python3
"""Real World Objects: Attributes & Capabilities

Dog Attributies (Fields/Variables): Height, Weight, Favorite Food

Dog Capabilities (Methods/Function): Run, Walk, Eat

Now a dog object is created from a template and that template is called a
 "class" and what will you do in these classes, you will define the attributes
 and capabilities of your dog object.
"""


class Dog:
    def __init__(self, name="", height=0, weight=0):
        '''"self" just allows an object to refer to itself just like you would
        refer to yourself as my so you would refer to my height, my weight & my
         favorite food, "self" is exactly the same as that. Why would we use th
        at? Well we are going to be able to create very custom dogs such as the
         dogs "spot". Well we are going to create "spot" using the template or
         class thet we define below(Dog class). But we must create the class
         before we name "spot" and this gets into the whole chicken or the egg
         sort of situation, we can not create a "spot" dog until we create a
         template that defines how to create dogs hence the use of the word
         "self"'''
        self.name = name
        self.height = height
        self.weight = weight

    def run(self):
        print("{} the dog runs".format(self.name))

    def eat(self):
        print("{} the dog eats".format(self.name))

    def bark(self):
        print("{} the dog barks".format(self.name))


def main():
    spot = Dog("Spot", 66, 26)
    spot.bark()

    bowser = Dog()
    bowser.bark()


main()
