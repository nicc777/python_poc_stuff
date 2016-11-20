from test.definitions.defs import Person

class Man(Person):
	def __init__(self, name='John Doe'):
		self.sex = 'M'
		self.name = name
		super(Man, self).__init__()

	def age(self):
		print('Always young at heart')


class Woman(Person):
	def __init__(self, name='Jane Doe'):
		self.sex = 'F'
		self.name = name
		super(Woman, self).__init__()

	def age(self):
		print('A woman never tells')


class SomeOtherClass:
	def __init__(self):
		pass

	def age(self):
		print('I should not ever work...')



