def grade_decorator(f):
	def wrapper(score, total):
		percent = f(score, total)

		grades = {
			5: 'A',
			4: 'A',
			3: 'B',
			2: 'C',
			1: 'D'
		}

		return percent, grades[percent // 20]
	return wrapper


class Student:
	def __init__(self, name, score, total):
		self.name = name
		self.__score = score    # score is made private
		self.total = total

    # our property methods for score    
	@property
	def score(self):
		print("Getting score...")
		return self.__score

	@score.setter
	def score(self, new_val):
		print("Setting new value...")
		self.__score = new_val

	@score.deleter
	def score(self, new_val):
		print("Deleting score...")
		del self.__score

    # our staticmethod get_percent. grade_decorator has been applied 
	@staticmethod
	@grade_decorator
	def get_percent(score, total):
		return score / total * 100

    # our classmethods, to allow different ways to create objects
	@classmethod
	def from_str(cls, str_arg):
		name, score, total = str_arg.split(',')
		return cls(name, int(score), int(total))

	@classmethod
	def from_tuple(cls, tup_arg):
		name, score, total = tup_arg
		return cls(name, score, total)

	def get_record(self):
		percent, grade = Student.get_percent(self.score, self.total)

		return f"Name: {self.name} | Percentage scored: {percent} % | Grade: {grade}"

	def __str__(self):
		return ("Name: " + str(self.name) + " Score: " + str(self.__score) + " Total : " + str(self.total))