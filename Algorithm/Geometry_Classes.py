import math

class Point:
	def __init__(self, x, y):
		self.x = x
		self.y = y
		if type(x) is int and type(y) is int:
			self.type = int
		else:
			self.type = float
	def __str__(self):
		if self.type is int:
			return "(%d, %d)" % (self.x, self.y)
		else:
			return "(%f, %f)" % (self.x, self.y)
	def __hash__(self):
		return hash((self.x, self.y))
	def __eq__(self, other):
		return type(other) is Point and self.x == other.x and self.y == other.y
	def __sub__(self, other):
		"""A - B ということなので、 vec(BA)を返す"""
		assert type(other) is Point, "type error."
		return Vector(self.x - other.x, self.y - other.y)

class Vector:
	def __init__(self, x, y):
		self.x = x
		self.y = y
		if type(x) is int and type(y) is int:
			self.type = int
		else:
			self.type = float
	def __str__(self):
		if self.type is int:
			return "(%d, %d)" % (self.x, self.y)
		else:
			return "(%f, %f)" % (self.x, self.y)
	def __hash__(self):
		return hash((self.x, self.y))
	def __eq__(self, other):
		return type(other) is Vector and self.x == other.x and self.y == other.y
	def __add__(self, other):
		assert type(other) is Vector, "type error."
		return Vector(self.x + other.x, self.y + other.y)
	def __sub__(self, other):
		assert type(other) is Vector, "type error."
		return Vector(self.x - other.x, self.y - other.y)
	def __mul__(self, other):
		"""内積"""
		assert type(other) is Vector, "type error."
		return self.x * other.x + self.y * other.y
	def __pow__(self, other):
		"""外積の大きさ"""
		assert type(other) is Vector, "type error."
		return self.x * other.y - self.y * other.y

class Line:
	def __init__(self, *args):
		def get_line(p1, p2):
			xs, ys = p1.x, p1.y
			xt, yt = p2.x, p2.y
			a = -(yt-ys)
			b = xt-xs
			c = (yt-ys)*xs - (xt-xs)*ys
			return a,b,c
		if len(args) == 3:
			a,b,c = args
		elif len(args) == 2 and type(args[0]) is Point and type(args[1]) is Point:
			assert args[0] != args[1], "given same points."
			a,b,c = get_line(*args)
		else: assert 0, "unkown argments are given."

		if type(a) is int and type(b) is int and type(c) is int:
			self.type = int
			if a < 0 or (a == 0 and b < 0) or (a == b == 0 and c < 0):
				a, b, c = -1*a, -1*b, -1*c
			g = math.gcd(math.gcd(a, b), c)
			a, b, c = a//g, b//g, c//g
		else:
			self.type = float
		self.a = a
		self.b = b
		self.c = c
		if type(a) is int and type(b) is int and type(c) is int:
			self.type = int
		else:
			self.type = float
	def __str__(self):
		if self.type is int:
			return "%dx + %dy + %d = 0" % (self.a, self.b, self.c)
		else:
			return "%fx + %fy + %f = 0" % (self.a, self.b, self.c)
	def __hash__(self):
		return hash((self.a, self.b, self.c))
	def __eq__(self, other):
		return type(other) is Line and self.a == other.a and self.b == other.b and self.c == other.c

p = Point(1,2)
v = Vector(1,2)
print(p==v)
