def sets():
    s1 = set([1,2,2,3])
    s2 = set([1,3,3,4])
    s3 = set([1,3])
    print("set s1: " + str(s1))
    print("set s2: " + str(s2))
    print("set s3: " + str(s3))
    print("Intersection, s1 & s2: " + str(s1 & s2))
    print("Union, s1 | s2: " + str(s1 | s2))
    print("Subset, s3 < s2: " + str(s3 < s2))
    print("Superset, s2 > s3: " + str(s2 > s3))
    print("difference, s1 - s2: " + str(s1 - s2))
    print("sym difference, s1 ^ s2: " + str(s1 ^ s2))
print("sets")
sets()