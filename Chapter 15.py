class Point:
    """ Point class represents and manipulates x,y coords. """

    def __init__(self, x=0, y=0):
        """ Create a new point at x, y """
        self.x = x
        self.y = y

    def distance_from_origin(self):
        """ Compute my distance from the origin """
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5

    def __str__(self):  # All we have done is renamed the method
        return "(this is a point x{0}, y{1})".format(self.x, self.y)


def print_point(pt):
    print("({0}, {1})".format(pt.x, pt.y))


p=Point(2,4)
q=Point(7,11)
print(p.x,p.y)
# p.x=2
# p.y=4

print(p.x,p.y,q.x,q.y)

print("(x={0}, y={1})".format(p.x, p.y))
distance_squared_from_origin = p.x * p.x + p.y * p.y
print("distance sq",distance_squared_from_origin)

pdist = p.distance_from_origin()
print("pdistance",pdist)

print_point(p)
print_point(q)

print(str(p))


class Point:
    """ Point class represents and manipulates x,y coords. """

    def __init__(self, x=0,y=0):
        """ Create a new point at the origin """
        self.x = x
        self.y = y

p=Point(2,3)
q=Point(7,11)
o=Point()

print(p.x,q.x,o.x )

