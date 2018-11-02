######################################################################################################################
# Name:
# Date:
# Description:
######################################################################################################################
from Tkinter import *
from math import sqrt, sin, cos, pi as PI
from random import randint
# the 2D point class
class Point(object):
	# the constructor
	def __init__(self, x=0.0, y=0.0):
		# initialize components with default (0.0,0.0)
		self.x = float(x)
		self.y = float(y)

	# accessors and mutators
	@property
	def x(self):
		return self._x

	@x.setter
	def x(self, value):
		self._x = value

	@property
	def y(self):
		return self._y

	@y.setter
	def y(self, value):
		self._y = value

	# calculates and returns the distance between two points
	def dist(self, other):
		return sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)

	# calculates and returns the midpoint between two points
	def midpt(self, other):
		return Point((self.x + other.x) / 2.0, (self.y + other.y) / 2.0)

	# calculates and returns a point that is a distance ratio between two points
	def interpt(self, other, r):
		# make sure that the distance ratio is expressed from a smaller component value to a larger one
		# first, the x-component
		rx = r
		if (self.x > other.x):
			rx = 1.0 - r
		# next, the y-component
		ry = r
		if (self.y > other.y):
			ry = 1.0 - r

		# calculate the new point's coordinates
		# the difference in the components (i.e., distance between the points) is first scaled by the specified distance ratio
		# the minimum of the components is then added back in order to obtain the coordinates in between the two points (and not with respect to the origin)
		x = abs(self.x - other.x) * rx + min(self.x, other.x)
		y = abs(self.y - other.y) * ry + min(self.y, other.y)

		return Point(x, y)

	# returns a string representation of the point: (x,y)
	def __str__(self):
		return "({},{})".format(self.x, self.y)

# the fractal superclass
class Fractal(object):
	# the constructor
	def __init__(self, dimensions):
		# the canvas dimensions
		self.dimensions = {"min_x" : 2, "min_y" : 2, "max_x" : 594, "max_y" : 514}
                self.dimensions["mid_x"] = ((self.dimensions["min_x"] + self.dimensions["max_x"]) / 2)
                self.dimensions["mid_y"] = ((self.dimensions["min_y"] + self.dimensions["max_y"]) / 2)
		# the default number of points to plot is 50,000
		self.num_points = 50000
		# the default distance ratio is 0.5 (halfway)
		self.r = 0.5

	# accessors and mutators
	@property
	def vertices(self):
		return self._vertices

	@vertices.setter
	def vertices(self, v):
		self._vertices = v

	# calculates and returns the x-coordinate of a point that is a distance ratio on the canvas horizontally
	def frac_x(self, r):
		return int((self.dimensions["max_x"] - self.dimensions["min_x"]) * r) + self.dimensions["min_x"]

	# calculates and returns the y-coordinate of a point that is a distance ratio on the canvas vertically
	def frac_y(self, r):
		return int((self.dimensions["max_y"] - self.dimensions["min_y"]) * r) + self.dimensions["min_y"]

# the Sierpinski triangle fractal class
# inherits from the fractal class
class SierpinskiTriangle(Fractal):
	# the constructor
	def __init__(self, canvas):
		# call the constructor in the superclass
		Fractal.__init__(self, canvas)
		# define the vertices based on the fractal size
		v1 = Point(self.dimensions["mid_x"], self.dimensions["min_y"])
		v2 = Point(self.dimensions["min_x"], self.dimensions["max_y"])
		v3 = Point(self.dimensions["max_x"], self.dimensions["max_y"])
		self.vertices = [ v1, v2, v3 ]

# the Sierpinski carpet fractal class
# inherits from the fractal class
class SierpinskiCarpet(Fractal):
	# the constructor
	def __init__(self, canvas):
		# call the constructor in the superclass
		Fractal.__init__(self, canvas)
		# define the vertices based on the fractal size
		v1 = Point(self.dimensions["min_x"], self.dimensions["min_y"])
		v2 = Point(self.dimensions["mid_x"], self.dimensions["min_y"])
		v3 = Point(self.dimensions["max_x"], self.dimensions["min_y"])
		v4 = Point(self.dimensions["min_x"], self.dimensions["mid_y"])
		v5 = Point(self.dimensions["max_x"], self.dimensions["mid_y"])
		v6 = Point(self.dimensions["min_x"], self.dimensions["max_y"])
		v7 = Point(self.dimensions["mid_x"], self.dimensions["max_y"])
		v8 = Point(self.dimensions["max_x"], self.dimensions["max_y"])
		self.vertices = [ v1, v2, v3, v4, v5, v6, v7, v8 ]
		# set the number of points for this fractal
		self.num_points = 100000
		# set the distance ratio for this fractal
		self.r = 0.66

# the pentagon fractal class
# inherits from the fractal class
class Pentagon(Fractal):
	# the constructor
	def __init__(self, canvas):
		# call the constructor in the superclass
		Fractal.__init__(self, canvas)
		# define the vertices based on the fractal size
		v1 = Point(self.dimensions["mid_x"] + self.dimensions["mid_x"] * cos(2 * PI / 5 + 60), (self.frac_y(0.5375) + self.dimensions["mid_y"] * sin(2 * PI / 5 + 60)))
		v2 = Point(self.dimensions["mid_x"] + self.dimensions["mid_x"] * cos(4 * PI / 5 + 60), (self.frac_y(0.5375) + self.dimensions["mid_y"] * sin(4 * PI / 5 + 60)))
		v3 = Point(self.dimensions["mid_x"] + self.dimensions["mid_x"] * cos(6 * PI / 5 + 60), (self.frac_y(0.5375) + self.dimensions["mid_y"] * sin(6 * PI / 5 + 60)))
		v4 = Point(self.dimensions["mid_x"] + self.dimensions["mid_x"] * cos(8 * PI / 5 + 60), (self.frac_y(0.5375) + self.dimensions["mid_y"] * sin(8 * PI / 5 + 60)))
		v5 = Point(self.dimensions["mid_x"] + self.dimensions["mid_x"] * cos(10 * PI / 5 + 60), (self.frac_y(0.5375) + self.dimensions["mid_y"] * sin(10 * PI / 5 + 60)))
		self.vertices = [ v1, v2, v3, v4, v5 ]
		# set the distance ratio for this fractal
		self.r = 0.618

# the hexagon fractal class
# inherits from the fractal class
class Hexagon(Fractal):
	# the constructor
	def __init__(self, canvas):
		# call the constructor in the superclass
		Fractal.__init__(self, canvas)
		# define the vertices based on the fractal size
		v1 = Point(self.dimensions["mid_x"], self.dimensions["min_y"])
		v2 = Point(self.dimensions["min_x"], self.frac_y(0.25))
		v3 = Point(self.dimensions["max_x"], self.frac_y(0.25))
		v4 = Point(self.dimensions["min_x"], self.frac_y(0.75))
		v5 = Point(self.dimensions["max_x"], self.frac_y(0.75))
		v6 = Point(self.dimensions["mid_x"], self.dimensions["max_y"])
		self.vertices = [ v1, v2, v3, v4, v5, v6 ]
		# set the distance ratio for this fractal
		self.r = 0.665

# the octagon fractal class
# inherits from the fractal class
class Octagon(Fractal):
	# the constructor
	def __init__(self, canvas):
		# call the constructor in the superclass
		Fractal.__init__(self, canvas)
		# define the vertices based on the fractal size
		v1 = Point(self.frac_x(0.2925), self.dimensions["min_y"])
		v2 = Point(self.frac_x(0.7075), self.dimensions["min_y"])
		v3 = Point(self.dimensions["min_x"], self.frac_y(0.2925))
		v4 = Point(self.dimensions["max_x"], self.frac_y(0.2925))
		v5 = Point(self.dimensions["min_x"], self.frac_y(0.7075))
		v6 = Point(self.dimensions["max_x"], self.frac_y(0.7075))
		v7 = Point(self.frac_x(0.2925), self.dimensions["max_y"])
		v8 = Point(self.frac_x(0.7075), self.dimensions["max_y"])
		self.vertices = [ v1, v2, v3, v4, v5, v6, v7, v8 ]
		# set the number of points for this fractal
		self.num_points = 75000
		# set the distance ratio for this fractal
		self.r = 0.705

