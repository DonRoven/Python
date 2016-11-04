import random
def city(x, y, n):
    n = 10
    list1 = [random.randint(1, n) for i in range(n*2)]
    list2 = [random.randint(1, n) for i in range(n*2)]
    zip(list1,list2)

print city(4, 6)


def find_pach(graf, start, end):
    path = []
    path += [start]
    if start == end:
        return path
    if not graph.has_key(start):
        return None
    for node in graph[start]:
        if node not in path:
            newpath = find_pach(graf, start, end)
            if newpath:
                return newpath
    return None