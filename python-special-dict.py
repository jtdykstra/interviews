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
orderedDict()