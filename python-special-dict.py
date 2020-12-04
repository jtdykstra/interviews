import collections

def orderedDict():
    od = collections.OrderedDict()
    od[1] = 1
    od[2] = 2
    od[3] = 3
    print(od)
    od.move_to_end(1)
    print("move key 1 to end " + str(od))
    od.popitem(last=False)
    print("pop first item " + str(od))

def dictProperties():
    d = {'a':1,'b':2,'c':3}

    print("d is {}".format(d))
    print("d.keys() {}".format(d.keys()))
    print("d.values() {}".format(d.values()))
    print("d.items() {}".format(d.items()))

orderedDict()
dictProperties()