import random

city1 = 8
city2 = 5
n = 10

list1 = [random.randint(1, n) for i in range(n)]
list2 = [random.randint(1, n) for i in range(n)]

cities = {}
for k, v in zip(list1,list2):
    if k in cities:
        cities[k].append(v) 
    else:
        cities[k] = [v]
for k, v in zip(list1,list2):
    if k not in cities:
        if v in cities:
            cities[v].append(k) 
        else:
            cities[v] = [k]

def check_direct_path(city1, city2, list1, list2):
    if x == list1[i] and y == list2[i] or x == list2[i] and y == list1[i]:
        return True
        print (city1, city2)
    else:
        return False


def check_path(city1, city2, cities):
    path = []
    path += [city1]
    if city1 == city2:
        return path
    if not cities.has_key(city1):
        return None
    for node in cities[city1]:
        if node not in path:
            newpath = find_pach(city1, city2, cities)
            if newpath:
                return newpath
    return None


print (check_path(8,5))