# Glen Paul Florendo
# COMPTNG16
# October 18, 2017

class MathVector:

	def __init__(self, *dimensions):
		self.components = []
		if len(dimensions) == 1:
			dim = dimensions[0]
			if type(dim) == int:
				self.components = [0, 0, 0, 0, 0]
			elif type(dim) == list:
				for d in dim:
					self.components.append(d)
		else:
			for d in dimensions:
				self.components.append(d)

