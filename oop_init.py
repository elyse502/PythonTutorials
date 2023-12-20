class Person:
	def __init__(self, name):
		self.name = name

	def say_hi(self):
		print('Hello, my name is', self.name)


p = Person('John Smith')
p.say_hi()
