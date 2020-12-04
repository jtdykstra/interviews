import collections

def namedTuples():
    Point = collections.namedtuple('Point', 'x y')
    point = Point(2,3)

    print("point x {} point y {}".format(point.x, point.y))

namedTuples()