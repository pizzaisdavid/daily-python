def contains_unique(iterable):
    for index, element in enumerate(iterable):
        if element in iterable[:index] + iterable[index + 1:]:
            return False
    return True      

for x in range(1000, 10000):
    s = str(x)
    combine = int(s[0:2]) + int(s[2:4])
    if x == combine * combine and contains_unique(str(x)):
        print x
