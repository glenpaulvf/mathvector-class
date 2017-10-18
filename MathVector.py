# Glen Paul Florendo
# COMPTNG16
# October 18, 2017

from math import sqrt

class MathVector:

    def __init__(self, *dimensions):
        self.components = []
        if len(dimensions) == 1:
            dim = dimensions[0]
            if type(dim) == int:
                self.components = [0, 0, 0, 0, 0]
            elif type(dim) == list or type(dim) == tuple:
                for d in dim:
                    self.components.append(d)
        else:
            for d in dimensions:
                self.components.append(d)

    def get_el(self, index):
    # returns the i-th component of the vector
        for i in range(len(self.components)):
            if i == index - 1:
                return self.components[i]

    def neg(self):
        return MathVector([-x for x in self.components])

    def mag(self):
        return sqrt(sum(map(lambda x: x*x, self.components)))

    def dot(self, other):
        return sum([x * y for x, y in zip(self.components, other.components)])

    def plus(self, other):
        return MathVector([x + y for x, y in zip(self.components, other.components)])

    def sp(self, scalar):
        return MathVector([x * scalar for x in self.components])

    def print_me(self):
        print self.components

    def __str__(self):
        return str(self.components)

